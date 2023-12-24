"""


Joe’s code problem on December 16th, 2023
Title: 17. Letter Combinations of a Phone Number
Tag: Hash Table, String, Backtracking
Difficulty: Medium

Given a string containing digits from 2-9 inclusive, return all possible letter stringList that the number could represent. Return the answer in any order.
A mapping of digits to digit2letters (just like on the telephone buttons) is given below. Note that 1 does not map to any digit2letters.


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
        # If the length of the digits is equal to 0, return an empty list.
        if len(digits) == 0:
            return []

        # Create a hashmap with a key representing the digit and a value representing its corresponding letters.
        digit2letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        # Define a backtrack function with two arguments: index and letterList.
        def backtrack(index, letterList):
            print("letter list:", letterList)
            print("string list:", stringList)
            # If the length of letterList is equal to the length of digits, 
            # join all letters within the letterList to form a complete string list and return it.
            if len(letterList) == len(digits):
                stringList.append("".join(letterList))
                print("string list after joining letter list:", stringList, '\n')
                return  # Backtrack

            # Iterate over the letters corresponding to a certain digit’s letters inside the hashmap. 
            # For each letter, perform the following steps to form different string combinations:
            for letter in digit2letters[digits[index]]:
                print("current index:", index)
                print("current digits[index]", digits[index])
                print("current digits:", digits)
                print("letter list:", letterList, '\n')
                print("current letter:", letter)
                # Append the letter to the letterList.
                letterList.append(letter)
                print("letter list after appending:", letterList, '\n')
                # Call the backtrack function again, 
                # increasing the index by one to add a different letter corresponding to a different digit.
                backtrack(index + 1, letterList)
                # Before adding a different letter corresponding to the same digit, 
                # remove the last letter in the letterList.
                letterList.pop()
                print("letter list after popping:", letterList, '\n')

        # Initialize an empty list for stringList.
        stringList = []
        # For the backtrack function, initially assign 0 to index and an empty list to letterList.
        backtrack(0, [])
        # Return the stringList.
        return stringList


S = Solution()

# combinations1 = S.letterCombinations("789")
# print(combinations1)

combinations2 = S.letterCombinations("23")
print(combinations2)

# combinations3 = S.letterCombinations("2")
# print(combinations3)
