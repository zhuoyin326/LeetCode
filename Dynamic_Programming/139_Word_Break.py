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

"""

# Top-Down Approach (Memoization)
class Solution1:
    def wordBreak(self, s, wordDict):
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
                print("start:", start, "end:", end, "dp(end):", dp(end), "s[start:end]", s[start:end])
                # If the substring is in the wordSet and the remaining string can be broken, return True
                if dp(end) and s[start:end] in wordSet:
                    print("start:", start, "end:", end, "dp(end):", dp(end), "s[start:end]", s[start:end])
                    memo[start] = True
                    print("start:", start, "memo:", memo)
                    return True

            # If no solution found, store False in the memo and return
            memo[start] = False
            print("start:", start, "memo:", memo)
            
            return False

        return dp(0)

s1 = Solution1()
result1 = s1.wordBreak("leetcode",["leet", "code"])
print("result1:", result1) 

"""

# Bottom-Up Approach
class Solution2:
    def wordBreak(self, s, wordDict):
        # Convert wordDict to a set for O(1) lookups
        wordSet = set(wordDict)
        n = len(s)
        # Initialize dp array where dp[end] is True if the first end characters can form a word
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be segmented

        # Iterate over the string
        for end in range(1, n + 1):
            print("end:", end)
            # Check each substring ending at end
            for start in range(end):
                # print("start:", start, "end:", end, "dp[end]:", dp[end], "s[start:end]", s[start:end])
                # If the substring s[start:end] is a word and dp[start] is True, set dp[end] to True
                if dp[start] and s[start:end] in wordSet:
                    print("start:", start, "end:", end, "s[0:start]:", s[0:start], "s[start:end]", s[start:end])
                    dp[end] = True
                    break

        return dp[n]

s2 = Solution2()
result2 = s2.wordBreak("leetcodeleetcode",["leet", "code"])
print("result2:", result2) 

