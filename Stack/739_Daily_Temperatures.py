"""
Joe’s code problem on April 27th, 2024
Title: 739. Daily Temperatures
Tag: Array, Stack, Monotonic Stack
Difficulty: Medium

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            print("curr_day:", curr_day, "curr_temp:", curr_temp)
            while stack and temperatures[stack[-1]] < curr_temp:
                print("stack:", stack, "stack[-1]:", stack[-1])
                print("temperatures[stack[-1]]:", temperatures[stack[-1]], "curr_temp:", curr_temp)
                prev_day = stack.pop()
                print("prev_day:", prev_day)
                answer[prev_day] = curr_day - prev_day
                print("answer[prev_day]:", answer[prev_day], "curr_day - prev_day:", curr_day - prev_day)
                print("answer:", answer)
            stack.append(curr_day)
            print("stack:", stack)
        
        return answer
    
s = Solution()
result = s.dailyTemperatures([73,74,75,71,69,72,76,73])
print("result:", result)