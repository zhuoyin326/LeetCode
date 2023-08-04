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
    	# Initialize count to 0. 
        # This variable will hold the total number of subarrays that sum up to k
        count = 0
        # Initialize largerPrefixSum to 0. 
        # This variable will keep track of the larger prefix sum while traversing the array
        largerPrefixSum = 0
        # Initialize smallerPrefixSums dictionary to keep track of smaller prefix sums and their counts
        # Key 0 is initialized with a count of 1 because smaller prefix sum 0 can be obtained by taking no elements
        smallerPrefixSums = {0: 1}

        # Iterate over each number in the nums array
        for num in nums:
            # Add the current number to largerPrefixSum
            largerPrefixSum += num

            # If largerPrefixSum - k is in smallerPrefixSums, 
            # This is because if there's a larger prefix sum j such that j - k exists in the array, 
            # it means that there are some subarrays ending at current index with sum k
            if largerPrefixSum - k in smallerPrefixSums:
                # add its count to our answer
                count += smallerPrefixSums[largerPrefixSum - k]

            # If largerPrefixSum is already a key in smallerPrefixSums,
            if largerPrefixSum in smallerPrefixSums:
                # increment its count
                smallerPrefixSums[largerPrefixSum] += 1
            # Otherwise, 
            else:
                # add largerPrefixSum to smallerPrefixSums with a count of 1
                smallerPrefixSums[largerPrefixSum] = 1

        # After traversing the entire array, return count
        # This will be the total number of contiguous subarrays that sum up to k
        return count

# Create a Solution object
s = Solution()

# Invoke the method (a function) within the Solution object
count = s.subarraySum([1, 2, 3], 3)

# Print the final results
print(count)