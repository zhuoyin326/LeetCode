"""
Joe’s code problem on July 3rd, 2022

Title: 15. 3Sum
Tag: Array, Two Pointers, Sorting
Difficulty: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

# Two Pointers Code:

from typing import List

class Solution:
    # This function finds all unique triplets in the array which gives the sum of zero.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the results (triplets).
        threeSumList = []  
        # Sort the numbers to use two-pointer technique efficiently.
        nums.sort()  
        
        # Iterate through the list to find the triplets.
        for i in range(len(nums)):
            # Since the list is sorted, if the current number is greater than 0, 
            # we won't find any triplets that sum up to 0.
            if nums[i] > 0:
                break
            # Avoid duplicates: Skip the same number to prevent duplicate triplets.
            if i == 0 or nums[i - 1] != nums[i]:
                # Call the helper function to find two numbers that, along with nums[i], sum to 0.
                self.twoSumII(nums, i, threeSumList)
        # Return the list of triplets found.
        return threeSumList  

    # Helper function to find two numbers such that they add up to the negative of the current number.
    def twoSumII(self, nums: List[int], i: int, threeSumList: List[List[int]]):
        
        # Start the left pointer just after index i.
        left = i + 1
        
        # Start the right pointer at the end of the list.
        right = len(nums) - 1
        
        # Continue until the two pointers meet.
        while (left < right):
            
            # Calculate the sum of the current triplet.
            sum = nums[i] + nums[left] + nums[right]  
            # If the sum is less than 0, move the left pointer to the right to increase the sum.
            if sum < 0:
                left += 1
            # If the sum is more than 0, move the right pointer to the left to decrease the sum.
            elif sum > 0:
                right -= 1
            else:
                # Found a triplet that sums up to 0, add it to the result list.
                threeSumList.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicate numbers to avoid duplicate triplets in the result.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1


# Hashmap Code:
class Solution:
    # The function aims to find all unique triplets in the list that sum up to zero.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This will hold the final list of triplets.
        threeSumList = []  
        # Sort the numbers to simplify finding triplets.
        nums.sort()  

        # Iterate over the list, using each number as a potential start of a triplet.
        for i in range(len(nums)):
            # If the current number is greater than 0, stop the loop.
            # Since the array is sorted, no further triplets that sum to 0 can be found.
            if nums[i] > 0:
                break
            # Skip duplicate values to avoid repeating the same triplet in the result.
            if i == 0 or nums[i - 1] != nums[i]:
                # Call the helper function to find two additional numbers to complete the triplet.
                self.twoSum(nums, i, threeSumList)
        # Return the list of triplets.
        return threeSumList  

    # Helper function to find pairs of numbers that, along with nums[i], sum to 0.
    def twoSum(self, nums: List[int], i: int, threeSumList: List[List[int]]):
        # A set to store numbers we've seen so far, for constant-time look-up.
        seen = set()  
        # Start searching for the second number of the triplet from the next index.
        j = i + 1  

        # Iterate over the remaining numbers in the list.
        while j < len(nums):
            # Calculate the value needed to complete the triplet.
            complement = -nums[i] - nums[j]  
            
            # If the needed value to complete the triplet is in the seen set,
            # it means we've found a valid triplet.
            if complement in seen:
                threeSumList.append([nums[i], nums[j], complement])  # Add the triplet to the result list.
                
                # Move past duplicate values to avoid duplicate triplets in the result.
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            
            # Mark the current number as seen.
            seen.add(nums[j])
            # Move to the next number.
            j += 1  