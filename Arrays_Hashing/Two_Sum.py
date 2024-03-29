"""
Joe’s code problem on April 3rd, 2022

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
    
"""

# Hashmap Code:

def twoSum(nums, target):
	# An empty dictionary stores all elements with their corresponding indices.
	dict = {}
	# A for loop traverses the list.
	for i in range(0, len(nums)):
        # The complement value is calculated as the difference between the target sum and the current element's value for each index.
		complement = target - nums[i]
		# If the complement value exists, the pair is found; the index of the complement value and the current index of the element are returned.
		if complement in dict:
			return [dict[complement], i]
		# If the complement value does not exist, nothing is returned.
		# The current element is stored as a key and its corresponding index as a value in the dictionary.
		dict[nums[i]] = i