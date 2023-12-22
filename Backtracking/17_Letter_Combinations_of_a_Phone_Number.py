"""


Joe’s code problem on December 16th, 2023
Title: 17. Letter Combinations of a Phone Number
Tag: Hash Table, String, Backtracking
Difficulty: Medium

Given a string containing digits from 2-9 inclusive, return all possible letter stringList that the number could represent. Return the answer in any order.
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

        def backtrack(index, letterList):
            print("letter list:", letterList)
            print("string list:", stringList)
            # If the current string is the same length as digits, we have a complete combination
            if len(letterList) == len(digits):
                stringList.append("".join(letterList))
                print("string list:", stringList, '\n')
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            for letter in num2letters[digits[index]]:
                # Add the letter to our current string
                print("current index:", index)
                print("current digits[index]", digits[index])
                print("current digits:", digits)
                print("letter list:", letterList, '\n')
                print("current letter:", letter)
                letterList.append(letter)
                print("letter list after appending:", letterList, '\n')
                # Move on to the next digit
                backtrack(index + 1, letterList)
                # Backtrack by removing the letter before moving onto the next
                letterList.pop()
                print("letter list after popping:", letterList, '\n')

        # Initiate backtracking with an empty string and starting index of 0
        stringList = []
        backtrack(0, [])
        return stringList


S = Solution()

# combinations1 = S.letterCombinations("789")
# print(combinations1)

combinations2 = S.letterCombinations("23")
print(combinations2)

# combinations3 = S.letterCombinations("2")
# print(combinations3)
