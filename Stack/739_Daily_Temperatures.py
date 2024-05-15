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

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Calculate the length of the temperature list.
        n = len(temperatures)
        # Initialize the variable to store the highest temperature observed as we iterate.
        hottest = 0
        # Initialize the answer list with zeros, where each zero represents the number of days until a warmer temperature.
        answer = [0] * n
        
        # Iterate over the temperature list in reverse order.
        for curr_day in range(n - 1, -1, -1):
            # Obtain the current day's temperature.
            current_temp = temperatures[curr_day]
            # Check if the current temperature is equal to or greater than the hottest temperature seen so far.
            if current_temp >= hottest:
                # Update the hottest temperature.
                hottest = current_temp
                # Since no warmer day is expected after the current hottest day, continue to the next iteration.
                continue
            
            # Initialize days counter to find the next warmer day.
            days = 1
            # Use previously calculated results to skip days that don't have a warmer temperature.
            while temperatures[curr_day + days] <= current_temp:
                # Skip the number of days until the next warmer day is found as per the 'answer' array.
                days += answer[curr_day + days]
            # Store the counted days in the answer for the current day.
            answer[curr_day] = days

        return answer