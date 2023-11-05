"""
    
Joe’s code problem on October 21th, 2023

Title: 704. Binary Search
Tag: Array, Binary Search
Difficulty: Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
    
"""

# Define the binary search function with a sorted sequence and target.
def binarySearch(nums, target):
	# Define the left boundary.
	left = 0
	# Define the right boundary.
	right = len(nums) - 1
	
# Continue the while loop as long as the left boundary is less than or equal to the right boundary.
	while left <= right:
		# Calculate the middle index using the left and right boundaries. 
		mid = (left + right)//2
		# Situation 1: If the number at the middle index is equal to the target.
		if nums[mid] == target:
			# Target found, return middle index.
			return mid
		# Situation 2: If the number at the middle index is greater than the target.
		elif nums[mid] > target:
			# Search in the lower range by updating the right boundary to mid-1. 
			right = mid - 1
		# Situation 3: If the number at the middle index is less than the target.
		else:
			# Search in the upper range by updating the left boundary to mid+1.
			left = mid + 1
	# If the target was not found after the while loop,  return -1.
	return -1


# Binary Search Lower Bound Code:
class Solution:
	def Search(nums, target):
		# we initialize the left pointer to 0.
		left = 0
		# Therefore, we initialize the right pointer to the length of the list.
		right = len(nums)
		# The while loop continues as long as the index of the left pointer is less than the index of the right pointer:
		while left < right:
			# Calculate the midpoint using the left and right pointers.
			mid = left + (right - left)/2
			# If the element at the midpoint is less than the target, move the left pointer to  ‘mid+1’.
			if nums[mid] < target:
				left = mid +1
			# If the element at the midpoint is greater than or equal to the target, the midpoint can be a potential insertion position, so we move the right pointer to ‘mid’ instead of ‘mid-1’.
			else:
				right = mid
		# If the left pointer is less than the length of the list and the element at the left pointer is equal to the target, we have found the leftmost insertion position for the target and return ‘left’.
		if left < len(nums) and nums[left] == target:
			return left
		# Otherwise, if we did not find the insertion position, we return ‘-1’.
		else:
			return -1

# Binary Search Upper Bound Code:
class Solution:
	def Search(nums, target):
		# we initialize the left pointer to 0.
		left = 0
		# Therefore, we initialize the right pointer to the length of the list.
		right = len(nums)
		# The while loop continues as long as the index of the left pointer is less than the index of the right pointer:
		while left < right:
			# Calculate the midpoint using the left and right pointers.
			mid = left + (right - left)/2
			# If the element at the midpoint is less than or equal to the target, move the left pointer to  ‘mid+1’.
			if nums[mid] < target:
				left = mid +1
			# If the element at the midpoint is greater than the target, the midpoint can be a potential insertion position, so we move the right pointer to ‘mid’ instead of ‘mid-1’.
			else:
				right = mid
		# If the left pointer is greater than 0 and the element at the left-1 is equal to the target, we have found the leftmost insertion position for the target and return ‘left-1’.
		if left > 0 and nums[left-1] == target:
			return left-1
		# Otherwise, if we did not find the insertion position, we return ‘-1’.
		else:
			return -1