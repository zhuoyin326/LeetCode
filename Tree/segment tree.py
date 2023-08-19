"""
Building the Segment Tree
"""

def build_tree(arr, tree, start, end, treeIndex):
    # Base case: If start equals end, it means we're at a leaf node
    if start == end:
        tree[treeIndex] = arr[start] # Set the value at this leaf node
    else:
        # Calculate the mid-point to divide the array into two halves
        mid = (start + end) // 2
        
        # Recursively build the left child segment tree
        build_tree(arr, tree, start, mid, 2*treeIndex + 1)
        
        # Recursively build the right child segment tree
        build_tree(arr, tree, mid+1, end, 2*treeIndex + 2)
        
        # The parent node's value is the sum of its children nodes
        tree[treeIndex] = tree[2*treeIndex + 1] + tree[2*treeIndex + 2]

"""
Querying the Segment Tree
"""
def query_tree(tree, start, end, l, r, treeIndex):
    # No overlap case: if the queried range is outside the current segment
    if r < start or l > end: 
        return 0
    
    # Total overlap case: if the queried range encompasses the current segment
    if l <= start and r >= end:
        return tree[treeIndex]
    
    # Calculate the mid-point
    mid = (start + end) // 2
    
    # Partial overlap: if the queried range partially overlaps with the left child
    left_sum = query_tree(tree, start, mid, l, r, 2*treeIndex + 1)
    
    # Partial overlap: if the queried range partially overlaps with the right child
    right_sum = query_tree(tree, mid+1, end, l, r, 2*treeIndex + 2)
    
    # Return the sum of results from left and right children
    return left_sum + right_sum


"""
Updating the Segment Tree
"""
def update_tree(arr, tree, start, end, treeIndex, arrIndex, value):
    # Base case: If we're at the exact treeIndex to be updated
    if start == end:
        arr[arrIndex] = value # Update the original array
        tree[treeIndex] = value # Update the segment tree node
    else:
        # Calculate the mid-point
        mid = (start + end) // 2
        
        # If the update treeIndex is in the left half, recursively update the left child
        if start <= arrIndex <= mid:
            update_tree(arr, tree, start, mid, 2*treeIndex + 1, arrIndex, value)
        # Otherwise, recursively update the right child
        else:
            update_tree(arr, tree, mid+1, end, 2*treeIndex + 2, arrIndex, value)
        
        # After updating child(ren), update the current node
        tree[treeIndex] = tree[2*treeIndex + 1] + tree[2*treeIndex + 2]


"""
Example Usage
"""
arr = [1, 2, 3, 4, 5] # Input array
n = len(arr) # Size of the input array
tree = [0] * (4 * n) # Segment tree, size 4n is a safe upper bound
build_tree(arr, tree, 0, n-1, 0) # Build the segment tree from the array

print(query_tree(tree, 0, n-1, 1, 3, 0)) # Query the sum from treeIndex 1 to 3. Expected output: 9

update_tree(arr, tree, 0, n-1, 0, 2, 6) # Update the element at treeIndex 2 to 6

print(query_tree(tree, 0, n-1, 1, 3, 0)) # Query the sum from treeIndex 1 to 3 again. Expected output: 12

