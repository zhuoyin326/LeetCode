"""


Joe’s code problem on December 16th, 2023
Title: 17. Letter Combinations of a Phone Number
Tag: Hash Table, String, Backtracking
Difficulty: Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to num2letters (just like on the telephone buttons) is given below. Note that 1 does not map to any num2letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
    
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the numbers to their corresponding letters
        num2letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, currString):
            print("current string:", currString)
            print("combinations:", combinations)
            # If the current string is the same length as digits, we have a complete combination
            if len(currString) == len(digits):
                combinations.append("".join(currString))
                print("combinations:", combinations, '\n')
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            for letter in num2letters[digits[index]]:
                # Add the letter to our current string
                print("index:", index)
                print("digits:", digits)
                print("current string:", currString, '\n')
                print("letter:", letter)
                currString.append(letter)
                print("current string after append:", currString, '\n')
                # Move on to the next digit
                backtrack(index + 1, currString)
                # Backtrack by removing the letter before moving onto the next
                currString.pop()
                print("current string after popping:", currString, '\n')

        # Initiate backtracking with an empty string and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations


S = Solution()

# combinations1 = S.letterCombinations("789")
# print(combinations1)

# combinations2 = S.letterCombinations("23")
# print(combinations2)

combinations3 = S.letterCombinations("2")
print(combinations3)
