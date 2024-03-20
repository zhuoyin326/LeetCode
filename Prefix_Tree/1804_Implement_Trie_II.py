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

# Define a class named TrieNode
class TrieNode:
    # Initialize a TrieNode instance
    # self refers to the instance of the TrieNode class
    def __init__(self):
        # Each trie node will store a dictionary of its children
        self.children = {}
        # Count of words ending at this node
        self.endOfWord = 0
        # Count of words having this node as prefix
        self.prefixCount = 0

# Define a class named Trie
class Trie:
    # Initialize a Trie instance
    # self refers to the instance of the Trie class
    def __init__(self):
        # The trie is initialized with a root trie node
        self.root = TrieNode()
    
    # Insert a word into the trie
    # self refers to the instance of the Trie class
    def insert(self, word: str) -> None:
        # Start at the root of the trie node
        # We use 'node' to keep track of the current character corresponding to the inserted word
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, add a new trie node
            if char not in node.children:
                node.children[char] = TrieNode()
            # If the character is in the node's children, we use the child node to update 'node'
            node = node.children[char]
            # Increment prefix count for the current node by one
            node.prefixCount += 1
        # Increase endOfWord of the last node by one after the for loop
        node.endOfWord += 1
    
    # Count the number of times a word is inserted in the trie
    # self refers to the instance of the Trie class
    def countWordsEqualTo(self, word: str) -> int:
        # Start at the root of the trie node.
        # We use 'node' to keep track of the current character corresponding to the searched word.
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, the word is not in the trie, so return 0.
            if char not in node.children:
                return 0
            # If the character is in the node's children, we use the child node to update 'node'.
            node = node.children[char]
        # After the for loop, we are at the end of the word, return the number of times a word is inserted. 
        return node.endOfWord
    
    # Count the number of words having the given prefix in the trie.
    # self refers to the instance of the Trie class
    def countWordsStartingWith(self, prefix: str) -> int:
        # Start at the root of the trie node
        # We use 'node' to keep track of the current character corresponding to the prefix.
        node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the node's children, then no word starts with this prefix, so return 0.
            if char not in node.children:
                return 0
            # If the character is in the node's children, we use the child node to update 'node'.
            node = node.children[char]
        # After the for loop, we are at the end of the prefix, return the number of words having the given prefix. 
        return node.prefixCount
    
    # Remove a word from the tire.
    # self refers to the instance of the Trie class
    def erase(self, word: str) -> None:
        # Start at the root of the trie node.
        # We use 'node' to keep track of the current character corresponding to the searched word.
        node = self.root
        # To keep track of nodes visited
        stack = []
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, nothing to erase.
            if char not in node.children:
                return
            # Add current node and character to stack.
            stack.append((node, char))  
            # If the character is in the node's children, we use the child node to update 'node'.
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
