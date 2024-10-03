"""
Joe’s code problem on October 5th, 2024
Title: 412. Fizz Buzz
Tag: Math, String, Simulation
Difficulty: Easy


Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
1 <= n <= 104

    
"""

from typing import List

# Naive Code:
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Initialize an empty list to store the answers.
        answer = []

        # Iterate i from 1 to n.
        for i in range(1, n+1):
            # If i is divisible by both 3 and 5, append "FizzBuzz" to the list.
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            # Else, if i is divisible by 3, append "Fizz" to the list.
            elif i % 3 == 0:
                answer.append("Fizz")
            # Else, if i is divisible by 5, append "Buzz" to the list.
            elif i % 5 == 0:
                answer.append("Buzz")
            # Else, when none of the above conditions are true, append i as a string to the list.
            else:
                answer.append(str(i))

        # At the end of the loop, return the answer list.
        return answer
    
    
# String Concatenation Code:
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Initialize an empty list to store the answers.
        answer = []

        # Iterate i from 1 to n.
        for i in range(1, n + 1):
            # Create an empty string for the current element.
            stringElement = ""

            # If i is divisible by 3, add "Fizz" to the current string.
            if i % 3 == 0:
                stringElement += "Fizz"
            # If i is divisible by 5, add "Buzz" to the current string.
            if i % 5 == 0:
                stringElement += "Buzz"
            # If the current string is still empty (i.e., i is not divisible by 3 or 5),
            # assign the string representation of i to the current string.
            if not stringElement:
                stringElement = str(i)
            # Append the current string to the answer list.
            answer.append(stringElement)
            
        # At the end of the loop, return the list of answers.
        return answer

