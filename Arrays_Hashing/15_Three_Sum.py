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
    # Three Sum Function: finds all unique triplets in the array which gives the sum of zero.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the triplet results.
        threeSumList = []  
        # Sort the numbers to use two-pointer technique efficiently.
        nums.sort()  
        
        # Iterate through the list to find the triplets.
        # The index 'i' is the first number.
        for i in range(len(nums)):
            # Since the list is sorted, if the current number is greater than 0, 
            # we won't find any triplets that sum up to 0.
            if nums[i] > 0:
                break
            # Avoid duplicates: Skip the same number to prevent duplicate triplets.
            if i == 0 or nums[i - 1] != nums[i]:
                # Call the two-sum II function to find two numbers that, along with nums[i], sum to 0.
                self.twoSumII(nums, i, threeSumList)
        # Return the list of triplets found.
        return threeSumList  

    # Two Sum II Function: finds two numbers such that they add up to the negative of the current number.
    def twoSumII(self, nums: List[int], i: int, threeSumList: List[List[int]]):
        
        # Start the left pointer just after index i.
        # 'left' is the index of the second number. 
        left = i + 1
        
        # Start the right pointer at the end of the list.
        # 'right' is the index of the third number.
        right = len(nums) - 1
        
        # Continue until the two pointers meet.
        while left < right:
            
            # Calculate the three-sum of the current triplet.
            three_sum = nums[i] + nums[left] + nums[right]  
            # If the three-sum is less than 0, move the left pointer to the right to increase the sum.
            if three_sum < 0:
                left += 1
            # If the three-sum is more than 0, move the right pointer to the left to decrease the sum.
            elif three_sum > 0:
                right -= 1
            # If the three-sum equals to 0, add it to the result list.  
            else:
                threeSumList.append([nums[i], nums[left], nums[right]])
                # Move both the left and right pointers to explore the next potential triplet.
                left += 1
                right -= 1
                # Skip duplicate numbers to avoid duplicate triplets in the result.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1



# Hashmap Code:
class Solution:
    # Three Sum Function: finds all unique triplets in the list that sum up to zero.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the triplet results.
        threeSumList = []  
        # Sort the numbers to simplify finding triplets.
        nums.sort()  

        # Iterate over the list, using each number as a potential start of a triplet.
        # The index 'i' is the first number.
        for i in range(len(nums)):
            # If the current number is greater than 0, stop the loop.
            # Since the array is sorted, no further triplets that sum to 0 can be found.
            if nums[i] > 0:
                break
            # Skip duplicate values to avoid repeating the same triplet in the result.
            if i == 0 or nums[i - 1] != nums[i]:
                # Call the two-sum function to find two additional numbers to complete the triplet.
                self.twoSum(nums, i, threeSumList)
        # Return the list of triplets.
        return threeSumList  

    # Two Sum Function: finds pairs of numbers that, along with nums[i], sum to 0.
    def twoSum(self, nums: List[int], i: int, threeSumList: List[List[int]]):
        # A set to store numbers we've seen so far, for constant-time look-up.
        seen = set()  
        # 'j' represents the second number, starting right after 'i'.
        j = i + 1  

        # Iterate over the remaining numbers in the list.
        while j < len(nums):
            # Calculate the complement needed to complete the triplet.
            complement = -nums[i] - nums[j]  
            
            # If the complement exists in the seen set, we have found a valid triplet.
            if complement in seen:
                # Add the triplet to the result list.
                threeSumList.append([nums[i], nums[j], complement])  
                
                # Skip over duplicate values for the second element to avoid duplicate triplets.
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            
            # If the complement does not exist in the seen set, add the current number to the seen set.
            seen.add(nums[j])
            # Move to the next number for the second element in the triplet.
            j += 1  