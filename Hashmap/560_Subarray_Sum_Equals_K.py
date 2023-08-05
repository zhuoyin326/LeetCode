"""

Joe’s code problem on August 5th, 2023

Title: 560. Subarray Sum Equals K
Tag: Array, Hash Table, Prefix Sum
Difficulty: Medium

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107  
    
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    	# Initialize the count of the subarrays with a sum equal to k to 0.
        count = 0
        # Initialize the prefix sum to 0.
        prefixSum = 0
        # Initialize the prefix sums dictionary to keep track of all the past prefix sum values (as dictionary keys) and their corresponding frequencies (as dictionary values).
        # Key 0 is initialized with a count of 1, because the prefix sum of 0 can be obtained by taking no elements.
        prefixSums = {0: 1}

        # Iterate over each number in the nums array
        for num in nums:
            # Add the current number from the nums array to the prefix sum
            prefixSum += num

            # If prefix sum - k can be found in the keys of the prefix sums dictionary
            if prefixSum - k in prefixSums:
                #  Add its frequency to the count of the subarray
                count += prefixSums[prefixSum - k]
                # This is because if there's a later prefix sum j such that j - k exists in the array, it means that there are some subarrays ending at current index with sum k

            # If the prefix sum is already a key in the prefix sums dictionary
            if prefixSum in prefixSums:
                # Increase its frequency by 1
                prefixSums[prefixSum] += 1
            # Otherwise
            else:
                # Add the prefix sum value as a key in the prefix sums dictionary with a count of 1
                prefixSums[prefixSum] = 1

        # After traversing the entire array, return the count of the subarrays with a sum equal to k.
        return count

# Create a Solution object
s = Solution()

# Invoke the method (a function) within the Solution object
count = s.subarraySum([-1, 2, 5, -3, -1, 1, 1], 2)

# Print the final results
print(count)