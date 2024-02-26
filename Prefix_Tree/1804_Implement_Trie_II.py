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
    def __init__(self):
        self.links = [None] * 26
        self.words_ending_here = 0
        self.words_starting_here = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            char_index = ord(w) - ord('a')
            if not node.links[char_index]:
                node.links[char_index] = TrieNode()
            node = node.links[char_index]
            node.words_starting_here += 1
        node.words_ending_here += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for w in word:
            char_index = ord(w) - ord('a')
            if not node.links[char_index]:
                return 0
            node = node.links[char_index]
        return node.words_ending_here

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for w in prefix:
            char_index = ord(w) - ord('a')
            if not node.links[char_index]:
                return 0
            node = node.links[char_index]
        return node.words_starting_here

    def erase(self, word: str) -> None:
        node = self.root
        for w in word:
            char_index = ord(w) - ord('a')
            node = node.links[char_index]
            node.words_starting_here -= 1
        node.words_ending_here -= 1