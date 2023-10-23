"""

Joe’s code problem on September 30th, 2023

Title: 22. Generate Parentheses
Tag: String, Dynamic Programming, Backtracking
Difficulty: Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8
   
"""
from typing import List
import collections

# Define the main class, Solution.
class Solution:
    # Define the primary function to generate parentheses combinations.
    def generateParenthesis(self, n: int) -> List[str]:
        # Define a function to check if a certain string is valid.
        def isValid(string):
            # Initialize a balance to keep track of the balance between open and close parentheses.
            balance = 0
            # Iterate over each character in the string.
            for char in string:
                # If the character is an open parenthesis
                if char == '(':
                    #  Increase the balance by one
                    balance += 1
                # If the character is a close parenthesis
                else:
                    # Decrease the balance by one
                    balance -= 1
                # If the balance is less than 0, it indicates the closed parenthesis count is more than the open parenthesis count
                if balance < 0:
                    # resulting in an invalid string
                    return False
            # After iterating over all characters in the string, if the balance is 0, then it's a valid string.
            return balance == 0

        # Initialize an empty list to store the results.
        result = []
        # Initialize a queue using deque with an empty string.
        queue = collections.deque([""])
        # Generate all parentheses combinations without considering their validity.
        # Continue the while loop as long as there is at least one element within the queue.
        while queue:
            # Remove and process the first string from the queue.
            string = queue.popleft()

            # If the length of the string is 2 * n
            if len(string) == 2 * n:
            # If the string is valid
                if isValid(string):
                    # Add the string to the result.
                    result.append(string)
                # If the string reaches a length of 2n or if it is invalid, skip the next two lines of code and proceed to the next iteration.
                continue
            # If the length of the string is less than 2*n, add a close parenthesis and enqueue.
            queue.append(string + ")")
            # If the length of the string is less than 2*n, add an open parenthesis and enqueue.
            queue.append(string + "(")
                    
        # Once all possible combinations have been evaluated, return the result.
        return result

# Create a Solution object
s = Solution()
# generate all combinations of well-formed parentheses
result = s.generateParenthesis(3)
# Print the final results
print("result:", result)

# Define the Solution class.
class Solution2:
    # Define the main function to generate all combinations of well-formed parentheses.
    def generateParenthesis(self, n: int) -> List[str]:
        # Define the backtrack function that tracks the three variables: the current string, the number of open parentheses, and the number of close parentheses.
        def backtrack(string, open, close):
            # If the current string reaches a length of 2n.
            if len(string) == 2 * n:
                # Add this valid string to the result.
                result.append(string)
                # Use a return without any expression when exiting a function early without returning any value.
                return
            # If the length of the current string is less than 2n, continue adding either open or close parentheses:
            # If the number of open parentheses is less than n.
            if open < n:
                # Append an open parenthesis to the current string and increase the count of open parentheses by one.
                backtrack(string + "(", open + 1, close)
            # If the number of close parentheses is less than the number of open parentheses.
            if close < open:
                # Append a close parentheses to the current string and increase the count of close parentheses by one.
                backtrack(string + ")", open, close + 1)
            # Initialize an empty list to store all valid parentheses.
            result = []
            # Initialize the backtrack function with an empty string and 0 for both open and close parentheses.
            backtrack("", 0, 0)
        # Return the final result.
        return result

# Create a Solution object
s2 = Solution2()
# generate all combinations of well-formed parentheses
result2 = s2.generateParenthesis(3)
# Print the final results
print("result 2:", result2)

