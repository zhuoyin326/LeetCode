"""
208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 
Example 1:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]

Explanation:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

"""


# Define a class named TrieNode
class TrieNode:
    # Initialize a TrieNode instance
    # self refers to the instance of the TrieNode class
    def __init__(self):
        # Each trie node will store a dictionary of its children
        self.children = {}
        # Indicates if the trie node represents the end of a word
        self.EndOfWord = False


# Define a class named Trie
class Trie:
	# Initialize a Trie instance
	# self refers to the instance of the Trie class
    def __init__(self):
        # The trie is initialized with a root trie node
        self.root = TrieNode()

    # Inserts a word into the trie
    # self refers to the instance of the Trie class
    def insert(self, word: str) -> None:
        # Start at the root of the trie node
        # We use 'node' to keep track of the current character corresponding to the inserted word
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, add a new trie node.
            if char not in node.children:
                node.children[char] = TrieNode()
            # If the character is in the node's children, we use the child node to update 'node'
            node = node.children[char]
        # Mark endOfWord of the last node as True after for loop
        node.EndOfWord = True

    # Search for a word in the trie.
    # self refers to the instance of the Trie class
    def search(self, word: str) -> bool:
        # Start at the root of the trie node
        # We use 'node' to keep track of the current character corresponding to the searched word.
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, the word is not in the trie, so return False.
            if char not in node.children:
                return False
            # If the character is in the node's children, we use the child node to update 'node'.
            node = node.children[char]
        # After the for loop, if we are at the end of the word, it means we have found the word in the trie; return True.
        # After the for loop, if we are in the middle of the word, it means we did not find the word in the trie; return False.
        return node.EndOfWord

    # Search for a prefix in the trie.
    # self refers to the instance of the Trie class
    def startsWith(self, prefix: str) -> bool:
        # Start at the root of the trie node
        # We use 'node' to keep track of the current character corresponding to the prefix
        node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the node's children, then no word starts with this prefix, so return False.
            if char not in node.children:
                return False
            # If the character is in the node's children, we use the child node to update 'node'.
            node = node.children[char]
        # Return True if the for loop completes without returning False, indicating the prefix is in the trie.
        return True
