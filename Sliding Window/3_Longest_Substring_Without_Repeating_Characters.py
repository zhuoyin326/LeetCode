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
        # Using set to store characters in current window
        # Initialize an empty set to track characters in the current window
        seen = set()  
        
        # Initializing two pointers and maxLength to keep track of longest substring length
        # 'l' and 'r' are the left and right of our current window, respectively
        l = 0
        r = 0
        maxLength = 0
        
        # While our right pointer hasn't reached the end of the string
        while r < len(s):  
            # If the current character at 'r' is not in our 'seen' set
            if s[r] not in seen:  
                # Add the current character to our set
                seen.add(s[r])  
                # Update maxLength with the length of the current window
                maxLength = max(maxLength, r - l + 1)  
                # Move the 'r' pointer to the right to expand the window
                r += 1  
            # If the current character at 'r' is in our 'seen' set (a repeating character)
            else:  
                # Remove the leftmost character of the current window from our set
                seen.remove(s[l]) 
                # Move the 'l' pointer to the right to shrink the window and remove the repeating character 
                l += 1  
        # Return the length of the longest substring without repeating characters     
        return maxLength  