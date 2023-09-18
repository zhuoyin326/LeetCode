"""

Joe’s code problem on September 16th, 2023
Title: 49. Group Anagrams
Tag: Array, Hash Table, String, Sorting
Difficulty: Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""
import collections
from typing import List

class SolutionOne:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	# Create an empty dictionary with key as the sorted string and value as the list of its anagrams
    anagramGroups = collections.defaultdict(list)
    # iterate over the list of all strings
    for s in strs:
	    # Use the sorted string as the dictionary key and append the original string to the list of anagrams under that key
        anagramGroups[tuple(sorted(s))].append(s)
    # return the values of the dictionary as a list
    return anagramGroups.values()


class SolutionTwo:
    def groupAnagrams(self, strs):
	    # Create an empty dictionary with key as the character count and value as the list of its anagrams
        anagramGroups = collections.defaultdict(list)
        
        # Iterate over the list of all strings
        for s in strs:
	        # Initialize a list for character count with the first index corresponding to ‘a’ and the last index corresponding to ‘z’
            charCount = [0] * 26
            # Iterate over the string
            for c in s:
	            # Calculate the count for all characters within the string
                charCount[ord(c) - ord('a')] += 1

            # Append the original string to the list of anagrams under that key
            anagramGroups[tuple(charCount)].append(s)
		
        # Return the values of the dictionary as a list
        return anagramGroups.values()

