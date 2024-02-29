"""
1804. Implement Trie II (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
void erase(String word) Erases the string word from the trie.
 
Example 1:

Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output
[null, null, null, 2, 2, null, 1, 1, null, 0]

Explanation
Trie trie = new Trie();
trie.insert("apple");               // Inserts "apple".
trie.insert("apple");               // Inserts another "apple".
trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
trie.erase("apple");                // Erases one "apple".
trie.countWordsEqualTo("apple");    // Now there is only one instance of "apple" so return 1.
trie.countWordsStartingWith("app"); // return 1
trie.erase("apple");                // Erases "apple". Now the trie is empty.
trie.countWordsStartingWith("app"); // return 0


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase.
It is guaranteed that for any function call to erase, the string word will exist in the trie.
"""

class TrieNode:
    # Each TrieNode contains a dictionary to hold its children and variables to count words and prefixes
    def __init__(self):
        # Map character to TrieNode
        self.children = {}
        # Count of words ending at this node
        self.endOfWord = 0
        # Count of words having this node as prefix
        self.prefixCount = 0

class Trie:
    # Trie data structure with root node initialization
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        # Insert a word into the trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # Increment prefix count for the current node
            node.prefixCount += 1
        # Mark the end of a word
        node.endOfWord += 1
    
    def countWordsEqualTo(self, word: str) -> int:
        # Return the number of times a word is inserted
        node = self.root
        for char in word:
            if char not in node.children:
                # Word not found
                return 0
            node = node.children[char]
        return node.endOfWord
    
    def countWordsStartingWith(self, prefix: str) -> int:
        # Return the number of words having the given prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                # Prefix not found
                return 0
            node = node.children[char]
        return node.prefixCount
    
    def erase(self, word: str) -> None:
        # Remove a word from the trie
        node = self.root
        # To keep track of nodes visited
        stack = []
        for char in word:
            if char not in node.children:
                # Word not found, nothing to erase
                return
            # Add current node and char to stack
            stack.append((node, char))  
            node = node.children[char]
        # Only decrement if word exists
        if node.endOfWord > 0:
            node.endOfWord -= 1
            # Walk back and update prefixCounts
            for node, char in reversed(stack):
                node.children[char].prefixCount -= 1
                if node.children[char].prefixCount == 0:
                    # Remove the node if no longer needed
                    del node.children[char]
