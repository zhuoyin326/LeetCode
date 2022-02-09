#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""

def longestCommonPrefix(stringList):
	stringListLength = len(stringList)
	if stringListLength == 0:
		return “”
	If stringListLength == 1:
		return stringList[0]
	stringList.sort()
	minLengthCommonChar = min(len(stringList[0]), len(stringList[-1]))
	charIndex = 0
	while (charIndex < minLengthCommonChar and stringList[0][charIndex] == stringList[-1][charIndex] ):
		charIndex += 1
	prefix = stringList[0][0:charIndex]
	return prefix

stringList1 = [“flower”, “flow”, “flight”]
stringList2 = [“dog”, “racecar”, “car”]

print(longestCommonPrefix(stringList1))

print(longestCommonPrefix(stringList2))

