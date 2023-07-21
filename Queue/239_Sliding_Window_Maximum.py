"""

Joe’s code problem on July 22th, 2023

Title: 239. Sliding Window Maximum
Tag: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
Difficulty: Hard

You are given an array of integers nums, there is a sliding dq of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the dq. Each time the sliding dq moves right by one position.
Return the max sliding dq.

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
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        
        # Process the indices of the input list covered by the first sliding dq
        for i in range(k):
            # Print index i
            print("the monotonic queue before appending:", dq)
            print("i for the first sliding dq:", i)
            # If (a) the current element is larger than or equal to the last elememt in the monotonic queue,
            # and (b) the monotonic queue is not empty.
            while dq and nums[i] >= nums[dq[-1]]:
                # Remove the last element from the monotonic queue
                poppedIndex = dq.pop()
                # Print the popped index
                print("popped index:", poppedIndex)
            dq.append(i)
            print("the monotonic queue after appending:", dq, "\n")

        # Add the maximum number within the first sliding dq to the result
        # Obtain the maximum number using the index of the first element in the monotonic queue 
        result.append(nums[dq[0]])
        # Print result after the first sliding dq
        print("result after the first sliding dq:", result, "\n")

        # Process the indices of the input list covered by the second sliding dq and beyond
        for i in range(k, len(nums)):
            print("i for the second sliding dq and beyond:", i)
            if dq and dq[0] == i - k:
                # 
                poppedLeftIndex = dq.popleft()
                # Print the popped index
                print("popped left index:", poppedLeftIndex)
            # If (a) the current element is larger than or equal to the last elememt in the monotonic queue, 
            # and (b) the monotonic queue is not empty.
            while dq and nums[i] >= nums[dq[-1]]:
                # Remove the last element from the monotonic queue
                poppedIndex = dq.pop()
                print("popped index:", poppedIndex)

            dq.append(i)
            print("the monotonic queue after appending:", dq, "\n")
            
            # Add the maximum number within the current sliding dq to the result
            # Obtain the maximum number using the index of first element in the monotonic queue 
            result.append(nums[dq[0]])
            
            # Print result after the second sliding dq and beyond
            print("result after the second sliding dq and beyond:", result, "\n")
            
        return result
    
# Create a Solution object
s = Solution()

# Find the maximum of all elements within each sliding dq
result = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)

# Print the final results
print("result:", result)

"""

# Import deque from collections module
from collections import deque

class Solution2:
    # Define a function that takes a list of integers, a dq size, and returns the max sliding window
    def maxSlidingWindow2(self, nums, k):
        # Initialize an empty list to store the results
        result = []
        # Initialize a deque to store the indices of the elements in the window
        dq = deque()
        # Loop through the list
        for i in range(len(nums)):
            # If the leftmost element in the dq is too far to the left boundary, pop it from the deque
            if dq and dq[0] <= i - k:
                print("deque:", dq, "index i:", i, "the leftmost element in the dq:", dq[0], "i-k:", i-k)
                poppedLeftElement = dq.popleft()
                print("popped left element:", poppedLeftElement, "dq after popping left:", dq)
            # While the deque is not empty and the current element is larger than the rightmost element 
            # in the window, pop the rightmost element from the deque
            while dq and nums[i] >= nums[dq[-1]]:
                print("deque:", dq, "num[i] > = nums[dq[-1]]:", nums[i], ">=", nums[dq[-1]])
                poppedElement = dq.pop()
                print("popped element:", poppedElement, "dq after popping:", dq)
            # Append the current index to the deque
            dq.append(i)
            print("index i append to the dq:", i, "deque after appending the index i:", dq)
            # If the window size is reached
            if i >= k - 1:
                # append the element at the leftmost index within the dq to the result list
                result.append(nums[dq[0]])
                print("result:", result, "nums[dq[0]]:", nums[dq[0]])
        # Return the result list
        return result


# Create a Solution object
s2 = Solution2()

# Find the maximum of all elements within each sliding dq
result2 = s2.maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3)

# Print the final results
print("result2:", result2)