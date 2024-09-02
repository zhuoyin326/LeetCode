"""
Joe’s code problem on March 23rd, 2024

Title: 167. Two Sum II - Input Array Is Sorted
Tag: Array, Two Pointers, Binary Search
Difficulty: Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

"""

from typing import List

class Solution:
    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        # self refers to an instance of the Solution class.
        
        # The left pointer starts at the beginning of the list.
        left = 0
        
        # The right pointer starts at the end of the list.
        right = len(numbers) - 1
        
        # Loop until the left pointer is to the left of the right pointer.
        while left < right:
            # Calculate the two-sum using the elements at the left and right pointers.
            two_sum = numbers[left] + numbers[right]
            
            # If the two-sum is less than the target, move the left pointer to the right to increase the sum.
            if two_sum < target:
                left += 1
 
            # If the two-sum is greater than the target, move the right pointer to the left to decrease the sum.
            elif two_sum < target:
                right -= 1

            # If the two-sum equals the target, return the indices (adjusted for 1-based indexing).
            else:
                return [left + 1, right + 1]
