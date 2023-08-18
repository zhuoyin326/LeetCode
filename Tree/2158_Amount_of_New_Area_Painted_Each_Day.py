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
    def __init__(self, n):
        # Initializing the segment tree with 0 values
        self.tree = [0] * ((1 << (math.ceil(math.log2(n)) + 1)) - 1)

    def query(self, segL, segR, queryL, queryR, treeInd):
        # Outside of the query range
        if queryR < segL or queryL > segR:
            return 0
        # If the current node has maximum capacity (i.e., segR-segL+1), we know all children
        # are fully populated so we don't need to traverse further
        if self.tree[treeInd] == segR - segL + 1:
            return min(segR, queryR) - max(queryL, segL) + 1
        # If the current segment is completely inside the query range
        if queryL <= segL and segR <= queryR:
            return self.tree[treeInd]
        # If the current segment is partially inside the query range
        mid = segL + (segR - segL) // 2
        l = self.query(segL, mid, queryL, queryR, 2 * treeInd + 1)
        r = self.query(mid + 1, segR, queryL, queryR, 2 * treeInd + 2)

        return l + r

    def update(self, segL, segR, queryL, queryR, treeInd):
        # If the node is at its maximum capacity
        if self.tree[treeInd] == segR - segL + 1:
            return 0
        oldV = self.tree[treeInd]
        # Outside of the update range
        if queryR < segL or queryL > segR:
            return 0
        # If the current segment is completely inside the update range
        if queryL <= segL and segR <= queryR:
            self.tree[treeInd] = segR - segL + 1
            diff = self.tree[treeInd] - oldV
            return diff
        # If the current segment is partially inside the update range
        mid = segL + (segR - segL) // 2
        diffL = self.update(segL, mid, queryL, queryR, 2 * treeInd + 1)
        diffR = self.update(mid + 1, segR, queryL, queryR, 2 * treeInd + 2)
        # Merge the results in the current node
        self.tree[treeInd] += diffL + diffR
        return self.tree[treeInd] - oldV

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # Constructing a segment tree where each node stores the count of the representing range
        l_len = 0
        for p in paint:
            l_len = max(l_len, p[1])

        segTree = SegmentTree(l_len + 1)

        # Calculate the result for each day
        res = []
        for p in paint:
            painted = segTree.query(0, l_len, p[0], p[1] - 1, 0)
            res.append(p[1] - p[0] - painted)
            segTree.update(0, l_len, p[0], p[1] - 1, 0)

        return res


# Create a Solution object
s = Solution()

# Invoke method with the Solution object
result = s.amountPainted([[1,4],[4,7],[5,8]])

# Print the result
print(result)