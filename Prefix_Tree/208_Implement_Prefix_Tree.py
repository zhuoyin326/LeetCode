"""

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


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        # Each node will store a dictionary of its children
        self.children = {}
        # Indicates if the node represents the end of a word
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # The trie is initialized with a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Start at the root
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, add a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the end of a word
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Start at the root
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, the word is not in the trie
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Check if we are at the end of a word
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # Start at the root
        node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the node's children, no word starts with this prefix
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # If we complete the loop, it means the prefix is in the trie
        return True
