"""

Joe’s code problem on August 12th, 2023

Title: 2158. Amount of New Area Painted Each Day
Tag: Array, Segment Tree, Ordered Set
Difficulty: Hard

There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.

Example 1:

Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1. 

Example 2:

Input: paint = [[1,4],[5,8],[4,7]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 5 and 8.
The amount of new area painted on day 1 is 8 - 5 = 3.
On day 2, paint everything between 4 and 5.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 5 - 4 = 1. 

Example 3:

Input: paint = [[1,5],[2,4]]
Output: [4,0]
Explanation:
On day 0, paint everything between 1 and 5.
The amount of new area painted on day 0 is 5 - 1 = 4.
On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.
The amount of new area painted on day 1 is 0.
 
Constraints:
1 <= paint.length <= 105
paint[i].length == 2
0 <= starti < endi <= 5 * 104    
        
"""

"""
from typing import List

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # Initialize an array with zeros to represent the painted area
        paintedArea = [0] * 50001
        # Initialize an array with zeros to store the painting length for each day of painting
        result = [0] * len(paint)
        
        # Iterate over the paint array to obtain start and end points for each painting day
        for i, (start, end) in enumerate(paint):
            
            print("i:", i, "start:", start, "end:", end, "\n")
            
            # When the current start point is smaller than the end point for the paint day
            while start < end:
                
                # There are 2 options for the next start point: either the next point or the value stored within the paintedArea array. 
                # We will compare both and assign the maximum of the two to the next start point.
                next = max(start + 1, paintedArea[start])
                print("next:", next, "start + 1:", start + 1, "paintedArea[start]:", paintedArea[start])
                
                # If the current start point of the paintedArea array has not been painted yet
                if paintedArea[start] == 0:
                    # Increase the painting length by 1 for that day
                    result[i] += 1
                    print("result[i]:", result[i])
                
                print("paintedArea[start]:", paintedArea[start])
                
                # Replace the value stored at the current start point with the maximum value between the value stored in the paintedArea array and the end point for the paint day
                paintedArea[start] = max(paintedArea[start], end)  # compression
                print("paintedArea[start]:", paintedArea[start], "end:", end)
                
                # Substitute the value of the current start point with the value of the next start point
                start = next
                print("start:", start, "next:", next, "\n")
        
        # Return the array that stores the painting length for each day of painting
        return result
"""

import math
from typing import List

class SegmentTree:
    # n refers to the size of the input array
    # The input array represents the maximum paint area
    def __init__(self, n):
        # Calculate the next power of 2 for n
        nextPowerOf2 = 2**math.ceil(math.log2(n))

        # Calculate the size of the segment tree array based on the size of the input array
        treeSize = 2 * nextPowerOf2 - 1

        # Initializing the segment tree with 0 values
        # 0 refers to the area that has not been painted before
        self.tree = [0] * treeSize
    
    # start and end refer to the start and end indices of the current segment tree node, respectively
    # l and r refer to the left and right indices of the query range, respectively
    # treeIndex represents the index of the current segment tree node in the segment tree array
    def query(self, start, end, l, r, treeIndex):
        # Scenarios A: If the query range [l, r] does not encompass the current segment represented by the node
        if r < start or l > end:
            # Return 0 for sum
            return 0
        
        # Scenario B: If the query range entirely or partially encompasses the current segment
        
        # If the current node has maximum capacity (i.e., end-start+1)
        # This means all leaf nodes under the current node have been painted
        if self.tree[treeIndex] == end - start + 1:
            # Calculate the painted area using the left and right boundaries of the encompassed segment area
            # The left boundary is calculated using the minimum of the "end paint area" and the right index of the query range
            # The right boundary is calculated using the maximum of the "start paint area" and the left index of the query range
            return min(end, r) - max(l, start) + 1
        # If the query range entirely encompasses the current segment
        if l <= start and end <= r:
            # Return the value of the current node
            return self.tree[treeIndex]
        # If the query range partially encompasses the current segment
        # Recursively query both the left and right children and combine their results
        # Find the midpoint of the current segment tree node using the start and end indices
        mid = start + (end - start) // 2
        # The index of the left child node in the segment tree array is 2*treeIndex + 1
        leftSum = self.query(start, mid, l, r, 2 * treeIndex + 1)
        # The index of the right child node in the segment tree array is 2*treeIndex + 2
        rightSum = self.query(mid + 1, end, l, r, 2 * treeIndex + 2)
        # Return the sum of results from left and right children
        return leftSum + rightSum

    # start and end refer to the start and end indices of the current segment tree node, respectively
    # l and r refer to the left and right indices of the query range, respectively
    # treeIndex represents the index of the current segment tree node in the segment tree array
    def update(self, start, end, l, r, treeIndex):
        # If the node is at its maximum capacity
        if self.tree[treeIndex] == end - start + 1:
            return 0
        # If the node is not at full capacity
        # Set the current value to old value
        oldValue = self.tree[treeIndex]
        # Outside of the update range
        if r < start or l > end:
            return 0
        # If the current segment is completely inside the update range
        if l <= start and end <= r:
            self.tree[treeIndex] = end - start + 1
            diff = self.tree[treeIndex] - oldValue
            return diff
        # If the current segment is partially inside the update range
        # Find the midpoint of the current segment tree node using the start and end indices
        mid = start + (end - start) // 2
        # The index of the left child node in the segment tree array is 2*treeIndex + 1
        LeftDiff = self.update(start, mid, l, r, 2 * treeIndex + 1)
        # The index of the right child node in the segment tree array is 2*treeIndex + 2
        RightDiff = self.update(mid + 1, end, l, r, 2 * treeIndex + 2)
        # Merge the results in the current node
        self.tree[treeIndex] += LeftDiff + RightDiff
        return self.tree[treeIndex] - oldValue

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # Construct a segment tree where each leaf node represents whether the corresponding paint area was painted or not
        # If painted, assign 1; otherwise, assign 0
        # Initialize maxPaintArea as 0
        maxPaintArea = 0
        # Iterate over the paint area for each day
        for p in paint:
            # Compare the current maxPaintArea with the "end paint area" for each day
            # Update maxPaintArea with the larger value
            maxPaintArea = max(maxPaintArea, p[1])

        # Instantiate the segment tree object using maxPaintArea
        segTree = SegmentTree(maxPaintArea + 1)

        # Calculate the result for each day
        result = []
        # Iterate over the paint area for each day
        for p in paint:
            # Query the segment tree with the start and end of the paint area for that day 
            # Determine the painted area within that range
            painted = segTree.query(0, maxPaintArea, p[0], p[1] - 1, 0)
            # The workload for that day: "end paint area" - "start paint area" - "previous painted area"
            result.append(p[1] - p[0] - painted)
            # Update the segment tree using the "start paint area" and the "end paint area"
            segTree.update(0, maxPaintArea, p[0], p[1] - 1, 0)

        return result


# Create a Solution object
s = Solution()

# Invoke method with the Solution object
result = s.amountPainted([[1,4],[4,7],[5,8]])

# Print the result
print(result)