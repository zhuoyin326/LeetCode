"""
Joe’s code problem on January 27th, 2024

Title: 139. Word Break
Tag: Array, Hash Table, String, Dynamic Programming, Trie, Memoization
Difficulty: Medium

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

    
"""


# Top-Down Approach (Memoization)
def wordBreak(s, wordDict):
    # Convert wordDict to a set for O(1) lookups
    wordSet = set(wordDict)
    memo = {}

    def dp(start):
        # If the start index reaches the end of the string, return True
        if start == len(s):
            return True

        # If the result is already in the memo, return it
        if start in memo:
            return memo[start]

        # Try every possible end index for the current substring
        for end in range(start + 1, len(s) + 1):
            # If the substring is in the wordSet and the remaining string can be broken, return True
            if s[start:end] in wordSet and dp(end):
                memo[start] = True
                return True

        # If no solution found, store False in the memo and return
        memo[start] = False
        return False

    return dp(0)


# Bottom-Up Approach
def wordBreak(s, wordDict):
    # Convert wordDict to a set for O(1) lookups
    wordSet = set(wordDict)
    n = len(s)
    # Initialize dp array where dp[end] is True if the first end characters can form a word
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can always be segmented

    # Iterate over the string
    for end in range(1, n + 1):
        # Check each substring ending at end
        for start in range(end):
            # If the substring s[start:end] is a word and dp[start] is True, set dp[end] to True
            if dp[start] and s[start:end] in wordSet:
                dp[end] = True
                break

    return dp[n]
