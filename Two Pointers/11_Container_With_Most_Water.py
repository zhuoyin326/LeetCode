"""

Joe’s code problem on September 23rd, 2023
Title: 11. Container With Most Water
Tag: Array, Two Pointers, Greedy
Difficulty: Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
    
"""
from typing import List

class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        # We initialize the maximum area to 0
        area = 0
        # We start the left and right boundaries at the leftmost and rightmost elements of the list
        left = 0
        right = len(height) - 1

        # As long as the left boundary is smaller than the right boundary, we continue the following while loop
        while left < right:
            # Calculate width of container by subtracting the left boundary from the right boundary
            width = right - left
            # Calculate the new area of the container by multiplying the width and the height of the container
            # Set the new maximum area to the greater of the new area and the previous maximum area.
            area = max(area, min(height[left], height[right]) * width)

            # If the left boundary is shorter than or equal to the right boundary
            if height[left] <= height[right]:
                # It is better to increase the left boundary by one, to increase the space
                left += 1
            # If the left boundary is taller than the right boundary
            else:
                # It is better to decrease the right boundary by one to increase the space
                right -= 1
        
        # After the while loop exits, return the maximum area
        return area
