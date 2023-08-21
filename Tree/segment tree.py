# Building the Segment Tree
def buildTree(arr, tree, start, end, treeIndex):
    # Base case: If start equals end, it means we're at a leaf node
    if start == end:
        # Set the value at this leaf node
        tree[treeIndex] = arr[start]
    else:
        # Calculate the mid-point to divide the array into two halves
        mid = (start + end) // 2
        
        # Recursively build the left child segment tree
        buildTree(arr, tree, start, mid, 2*treeIndex + 1)
        
        # Recursively build the right child segment tree
        buildTree(arr, tree, mid+1, end, 2*treeIndex + 2)
        
        # The parent node's value is the sum of its children nodes
        tree[treeIndex] = tree[2*treeIndex + 1] + tree[2*treeIndex + 2]


# Querying the Segment Tree
def queryTree(tree, start, end, l, r, treeIndex):
    #  If the query range [l, r] does not encompass the current segment represented by the node
    if r < start or l > end: 
        # Return an identity value (e.g., 0 for sum, infinity for minimum)
        return 0
    
    # If the query range entirely encompasses the current segment
    if l <= start and r >= end:
        # Return the value of the current node
        return tree[treeIndex]
    
    # If the query range partially encompasses the current segment
    # Recursively query both the left and right children and combine their results.
    
    # Calculate the mid-point
    mid = (start + end) // 2
    
    # If the query range partially encompasses the left child
    leftSum = queryTree(tree, start, mid, l, r, 2*treeIndex + 1)
    
    # If the query range partially encompasses the right child
    rightSum = queryTree(tree, mid+1, end, l, r, 2*treeIndex + 2)
    
    # Return the sum of results from left and right children
    return leftSum + rightSum


# Updating the Segment Tree
def updateTree(arr, tree, start, end, treeIndex, arrIndex, value):
    # Base case: If we're at the exact treeIndex to be updated
    if start == end:
        # Update the original array
        arr[arrIndex] = value
        # Update the segment tree node
        tree[treeIndex] = value
    else:
        # Calculate the mid-point
        mid = (start + end) // 2
        
        # If the update treeIndex is in the left half
        if start <= arrIndex <= mid:
            # Recursively update the left child
            updateTree(arr, tree, start, mid, 2*treeIndex + 1, arrIndex, value)
        # Otherwise
        else:
            # Recursively update the right child
            updateTree(arr, tree, mid+1, end, 2*treeIndex + 2, arrIndex, value)
        
        # After updating child(ren), update the current node
        tree[treeIndex] = tree[2*treeIndex + 1] + tree[2*treeIndex + 2]


# Example Usage

# Input array
arr = [1, 2, 3, 4, 5] 

# Size of the input array
n = len(arr) 

# Segment tree, size 4n is a safe upper bound
tree = [0] * (4 * n) 

# Build the segment tree from the array
buildTree(arr, tree, 0, n-1, 0) 

# Query the sum from treeIndex 1 to 3. Expected output: 9
print(queryTree(tree, 0, n-1, 1, 3, 0)) 

# Update the element at treeIndex 2 to 6
updateTree(arr, tree, 0, n-1, 0, 2, 6) 

# Query the sum from treeIndex 1 to 3 again. Expected output: 12
print(queryTree(tree, 0, n-1, 1, 3, 0)) 

