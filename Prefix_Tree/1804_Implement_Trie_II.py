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

# Define a class named TrieNode to represent nodes in a Trie.
class TrieNode:
    # Constructor to initialize a TrieNode instance.
    # 'self' refers to the instance of the TrieNode class.
    def __init__(self):
        # Each trie node has a dictionary 'children' to store its child nodes.
        self.children = {}
        # Integer 'endOfWord' to count the number of words ending at this node.
        self.endOfWord = 0
        # Integer 'prefixCount' to count the number of words that have this node as a prefix.
        self.prefixCount = 0

# Define a class named Trie for the trie data structure.
class Trie:
    # Constructor to initialize a Trie instance.
    # 'self' refers to the instance of the Trie class.
    def __init__(self):
        # Initialize the trie with a root node.
        self.root = TrieNode()
    
    # Method to insert a word into the trie.
    # 'self' refers to the instance of the Trie class.
    def insert(self, word: str) -> None:
        # Begin traversal from the root node.
        # 'node' keeps track of the traversal's current node.
        node = self.root
        # Traverse each character in 'word'.
        for char in word:
            # If the character is not present, add a new TrieNode as its child.
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node corresponding to the character.
            node = node.children[char]
            # Increment 'prefixCount' of the current node.
            node.prefixCount += 1
        # Increment 'endOfWord' to signify the end of a word.
        node.endOfWord += 1
    
    # Method to count the occurrences of a word in the trie.
    # 'self' refers to the instance of the Trie class.
    def countWordsEqualTo(self, word: str) -> int:
        # Begin traversal from the root node.
        # 'node' keeps track of the current node for the search.
        node = self.root
        # Traverse each character in 'word'.
        for char in word:
            # If the character is missing, the word does not exist in the trie.
            if char not in node.children:
                return 0
            # Move to the child node corresponding to the character.
            node = node.children[char]
        # Return the count of the word's occurrences.
        return node.endOfWord
    
    # Method to count words that start with a given prefix in the trie.
    # 'self' refers to the instance of the Trie class.
    def countWordsStartingWith(self, prefix: str) -> int:
        # Begin traversal from the root node.
        # 'node' keeps track of the current node for the search.
        node = self.root
        # Traverse each character in 'prefix'.
        for char in prefix:
            # If the character is missing, no word starts with the prefix.
            if char not in node.children:
                return 0
            # Move to the child node corresponding to the character.
            node = node.children[char]
        # Return the count of words starting with the prefix.
        return node.prefixCount
    
    # Method to remove a word from the trie.
    # 'self' refers to the instance of the Trie class.
    def erase(self, word: str) -> None:
        # Begin traversal from the root node.
        # 'node' keeps track of the current node for the search.
        node = self.root
        # Stack to keep track of nodes visited during traversal.
        stack = []
        # Traverse each character in 'word'.
        for char in word:
            # If the character is missing, the word is not present.
            if char not in node.children:
                return
            # Add the current node and character to the stack.
            stack.append((node, char))
            # Move to the child node corresponding to the character.
            node = node.children[char]
            
        # At the end of the word, if 'endOfWord' > 0, the word exists.
        if node.endOfWord > 0:
            # Decrement 'endOfWord' to remove one occurrence of the word.
            node.endOfWord -= 1
            # Walk back through the stack to update 'prefixCount's.
            for node, char in reversed(stack):
                node.children[char].prefixCount -= 1
                # If 'prefixCount' reaches 0, remove the child node as it's unnecessary.
                if node.children[char].prefixCount == 0:
                    del node.children[char]