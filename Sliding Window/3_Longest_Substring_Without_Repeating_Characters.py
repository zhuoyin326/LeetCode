"""
Joe’s code problem on September 2rd, 2023

Title: 3. Longest Substring Without Repeating Characters
Tag: Hash Table, String, Sliding Window
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use an empty set, named seen, to keep track of non-repeating characters within the current substring
        seen = set()

        # Use two pointers, l and r, to define the left and right boundaries of the current substring
        # Initialize both l and r to 0
        l = 0
        r = 0
        # Let maxLength represent the length of the longest substring without repeating characters
        # Initialize maxLength to 0
        maxLength = 0

        # Execute a while loop as long as the right pointer r has not reached the end of the string
        while r < len(s):
            # If the character at the right pointer is not in the seen set
            # It means we have found a new non-repeating character
            if s[r] not in seen:
                # Add this character to the seen set
                seen.add(s[r])
                # Update the maxLength if the current substring’s length (r - l + 1) is greater than maxLength
                maxLength = max(maxLength, r - l + 1)
                # Move the right pointer, r, one step to the right to expand the current sliding window
                r += 1
            # If the character at the right pointer is already in the seen set, this indicates a repetition
            else:
                # Remove the character at the left pointer, l, from the seen set
                seen.remove(s[l])
                # Move the left pointer, l,  one step to the right to shrink the current sliding window
                l += 1
        # Once the while loop completes, return maxLength
        return maxLength
