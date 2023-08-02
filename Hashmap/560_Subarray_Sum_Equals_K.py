"""

Joe’s code problem on August 5th, 2023
Title: 560. Subarray Sum Equals K
Tag: Array, Graph, Heap (Priority Queue), Shortest Path
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

def subarraySum(nums, k):
    # Initialize count to 0. 
    # This variable will hold the total number of subarrays that sum up to k
    count = 0

    # Initialize cumulative_sum to 0. 
    # This variable will keep track of the cumulative sum while traversing the array
    cumulative_sum = 0

    # Initialize sum_dict dictionary to keep track of cumulative sums and their counts
    # Key 0 is initialized with a count of 1 because sum 0 can be obtained by taking no elements
    sum_dict = {0: 1}

    # Iterate over each number in the nums array
    for num in nums:
        # Add the current number to cumulative_sum
        cumulative_sum += num

        # If cumulative_sum - k is in sum_dict, add its count to our answer
        # This is because if there's a cumulative sum j such that j - k (i.e., the current cumulative_sum) exists in the array,
        # it means that there are some subarrays ending at current index with sum k
        if cumulative_sum - k in sum_dict:
            count += sum_dict[cumulative_sum - k]

        # If cumulative_sum is already a key in sum_dict, increment its count
        # Otherwise, add cumulative_sum to sum_dict with a count of 1
        if cumulative_sum in sum_dict:
            sum_dict[cumulative_sum] += 1
        else:
            sum_dict[cumulative_sum] = 1

    # After traversing the entire array, return count
    # This will be the total number of contiguous subarrays that sum up to k
    return count
