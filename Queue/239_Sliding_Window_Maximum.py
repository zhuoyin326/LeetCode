"""

Joe’s code problem on July 22th, 2023

Title: 239. Sliding Window Maximum
Tag: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
Difficulty: Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position	Max
------------------------	-----
[1  3  -1] -3  5  3  6  7      3
 1 [3  -1  -3] 5  3  6  7      3
 1  3 [-1  -3  5] 3  6  7      5
 1  3  -1 [-3  5  3] 6  7      5
 1  3  -1  -3 [5  3  6] 7      6
 1  3  -1  -3  5 [3  6  7]     7

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        
        # Process the indices of the input list covered by the first sliding window
        for i in range(k):
            # Print index i
            print("the monotonic queue before appending:", dq)
            print("i for the first sliding window:", i)
            while dq and nums[i] >= nums[dq[-1]]:
                # Remove the last element from the monotonic queue
                poppedIndex = dq.pop()
                # Print the popped index
                print("popped index:", poppedIndex)
            dq.append(i)
            print("the monotonic queue after appending:", dq)

        # Add the maximum number within the first sliding window to the result
        # Obtain the maximum number using the index of the first element in the monotonic queue 
        result.append(nums[dq[0]])
        # Print result after the first sliding window
        print(result)

        # Process the indices of the input list covered by the second sliding window and beyond
        for i in range(k, len(nums)):
            print("i for the second sliding window and beyond", i)
            if dq and dq[0] == i - k:
                # 
                poppedLeftIndex = dq.popleft()
                # Print the popped index
                print("popped left index:", poppedLeftIndex)
            while dq and nums[i] >= nums[dq[-1]]:
                # Remove the last element from the monotonic queue
                poppedIndex = dq.pop()
                print("popped index:", poppedIndex)

            dq.append(i)
            print("the monotonic queue after appending:", dq)
            
            # Add the maximum number within the current sliding window to the result
            # Obtain the maximum number using the index of first element in the monotonic queue 
            result.append(nums[dq[0]])
            
            # Print result after the second sliding window and beyond
            print(result)
            
        return result
    
# Create a Solution object
s = Solution()

# Find the maximum of all elements within each sliding window
result = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)

# Print the final results
print(result)
