"""
Joe’s code problem on March 30th, 2024

Title: 18. 4Sum
Tag: Array, Two Pointers, Sorting
Difficulty: Medium

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

# Two Pointers Code:
from typing import List
class Solution:
    # Define a method fourSum inside the Solution class. It takes a list of integers and a target integer, returning a list of lists of integers.
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
	
        # Define a helper function for finding k-sum combinations. 
        # It is a recursive function that reduces the problem of k-sum to 2-sum.
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            # This will hold the result of the k-sum combinations.
            kSumList = []  
            
            # Base case: if nums is empty, simply return an empty list since no sums can be found.
            if not nums:
                return kSumList
            
            # Check if the target value is achievable with the current k elements. 
            # The lowest possible sum is obtained by adding the smallest k numbers (k*nums[0]) and the highest by adding the largest k numbers (k*nums[-1]). 
            # If the target is smaller than the smallest possible sum or larger than the largest possible sum, 
            # it's impossible to find a combination that meets the target, so return an empty list as there are no valid combinations.
            if target < k*nums[0] or k*nums[-1] < target:
                return kSumList
            
            # Base case of recursion: when k is 2, use the twoSum method to find pairs that sum to target.
            if k == 2:
                return twoSum(nums, target)
    
            # Recursive case: for each number in nums, try to find (k-1)-sums in the remaining list that sum up with nums[i] to target.
            for i in range(len(nums)):
                # To avoid duplicate results, skip numbers that are the same as the previous number.
                if i == 0 or nums[i - 1] != nums[i]:
                    # Recursive call for (k-1)-Sum with the remaining list and adjusted target.
                    for remainingList in kSum(nums[i + 1:], target - nums[i], k - 1):
                        # If a valid subset is found, add the current number to it.
                        kSumList.append([nums[i]] + remainingList)
    
            return kSumList

        # Define a twoSum function, used as the base case for the kSum function.
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            # Result list for storing pairs
            twoSumList = []  
            
            # The left pointer starts at the beginning of the list.
            left = 0
        
            # The right pointer starts at the end of the list.
            right = len(nums) - 1
    
            # Loop until the left pointer is to the left of the right pointer.
            while left < right:
                # Calculate the sum using the elements at the left and right pointers.
                sum = nums[left] + nums[right]  
                
                # If the sum is less than the target, move the left pointer to the right to increase the sum.
                # Avoid duplicates.
                if sum < target or (left > 0 and nums[left] == nums[left - 1]):
                    left += 1
                    
                # If the sum is greater than the target, move the right pointer to the left to decrease the sum.
                # Avoid duplicates.
                elif sum > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                    right -= 1
                    
                # If the sum equals the target, a pair is found.
                else:
                    # Add it to the result list and move both pointers.
                    twoSumList.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                                                         
            return twoSumList

        # Sort the nums list to facilitate the twoSum approach and make it easier to avoid duplicates.
        nums.sort()  
        # Call the kSum function initially for k=4 to find quadruplets.
        return kSum(nums, target, 4)  

s1 = Solution()
results = s1.fourSum( [1,0,-1,0,-2,2], 0)
print(results)


# Hashmap Code:
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Define a helper function for finding k-sum combinations. 
        # It is a recursive function that reduces the problem of k-sum to 2-sum.
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            # This will hold the result of the k-sum combinations.
            kSumList = []  
            
            # Base case: if nums is empty, simply return an empty list since no sums can be found.
            if not nums:
                return kSumList
    
            # Check if the target value is achievable with the current k elements. 
            # The lowest possible sum is obtained by adding the smallest k numbers (k*nums[0]) and the highest by adding the largest k numbers (k*nums[-1]). 
            # If the target is smaller than the smallest possible sum or larger than the largest possible sum, 
            # it's impossible to find a combination that meets the target, so return an empty list as there are no valid combinations.
            if target < k*nums[0] or k*nums[-1] < target:
                return kSumList
            
            # Base case for recursion: when k is 2, use the twoSum method to find pairs that sum to target.
            if k == 2:
                return twoSumII(nums, target)
    
            #  Recursive case: for each number in nums, try to find (k-1)-sums in the remaining list that sum up with nums[i] to target.
            for i in range(len(nums)):
                # To avoid duplicate results, skip numbers that are the same as the previous number.
                if i == 0 or nums[i - 1] != nums[i]:
                    # Recursive call for (k-1)-Sum with the remaining list and adjusted target.
                    for remainingList in kSum(nums[i + 1:], target - nums[i], k - 1):
                        # If a valid subset is found, add the current number to it.
                        kSumList.append([nums[i]] + remainingList)
            return kSumList

        # Define a twoSum function, used as the base case for the kSum function.
        def twoSumII(nums: List[int], target: int) -> List[List[int]]:
            # Result list for storing pairs
            twoSumList = []
            # Use a set to track numbers we've seen.  
            s = set()  
    
            for i in range(len(nums)):
                # Check if the complement exists in the set to form a pair with the current number.
                if len(twoSumList) == 0 or twoSumList[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        twoSumList.append([target - nums[i], nums[i]])
                # Add the current number to the set.
                s.add(nums[i])  
    
            return twoSumList
        # Sort the nums list to facilitate the twoSum approach and make it easier to avoid duplicates.
        nums.sort()
        # Call the kSum function initially for k=4 to find quadruplets.
        return kSum(nums, target, 4)