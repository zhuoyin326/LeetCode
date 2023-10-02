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

# Define the main class Solution.
class Solution:
    # Define the primary function to generate parenthesis combinations.
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Nested helper function to check if a given parenthesis string is valid.
        def isValid(string):
            # Initialize a counter to keep track of unmatched open parentheses.
            balance = 0
            # Iterate over each character in the string.
            for char in string:
                # If the character is an opening parenthesis, increment the counter.
                if char == '(':
                    balance += 1
                # If it's a closing parenthesis, decrement the counter.
                else:
                    balance -= 1
                # If at any point there are more closing than opening parentheses, it's invalid.
                if balance < 0:
                    return False
            # If after processing all characters, the count is 0, then it's a valid string.
            return balance == 0
        
        # Initialize a list to store all valid parenthesis combinations.
        answer = []
        # Initialize a queue using deque to assist in generating the combinations.
        queue = collections.deque([""])
        # Continue processing until all combinations in the queue have been evaluated.
        while queue:
            # Remove and process the first string from the queue.
            string = queue.popleft()

            # If the length of string is 2 * n, add it to `answer` if it's valid.
            # This length means we've added `n` open and `n` close brackets, so it's a complete string.
            if len(string) == 2 * n:
                # Use the helper function to check if it's a valid string.
                if isValid(string):
                    answer.append(string)
                # If it's not valid or once added, skip to the next iteration.
                continue
            # If the string is not of length 2*n, then add a closing parenthesis and enqueue.
            queue.append(string + ")")
            # Also, add an opening parenthesis and enqueue.
            queue.append(string + "(")
            
        # Once all possible combinations have been evaluated, return the valid ones.
        return answer


# Define the Solution class
class Solution:
    
    # Define the main function to generate all combinations of well-formed parentheses
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Define a helper function for backtracking
        def backtrack(string, open, close):
            
            # Base condition: If the current string's length is equal to 2n (n pairs of parentheses)
            if len(string) == 2 * n:
                
                # Add the valid string to the result list
                result.append(string)
                return
            
            # If the count of open brackets used so far is less than n
            if open < n:
                
                # Append a open bracket and make a recursive call to continue the exploration
                backtrack(string + "(", open + 1, close)
            
            # If the count of close brackets used so far is less than the count of open brackets
            if close < open:
                
                # Append a close bracket and make a recursive call to continue the exploration
                backtrack(string + ")", open, close + 1)

        # Initialize the result list to store all valid combinations
        result = []
        
        # Start the backtracking with an empty string and 0 counts for both open and close brackets
        backtrack("", 0, 0)
        
        # Return the final list of valid combinations
        return result
