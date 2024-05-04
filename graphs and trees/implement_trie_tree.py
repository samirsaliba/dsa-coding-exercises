# 208. Implement Trie (Prefix Tree)

# A trie (pronounced as "try") or prefix tree is a tree data structure 
# used to efficiently store and retrieve keys in a dataset of strings. 
# There are various applications of this data structure, 
# such as autocomplete and spellchecker.

# Implement the Trie class:

#Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.

# boolean startsWith(String prefix) Returns true if 
# there is a previously inserted string word that has the prefix prefix, 
# and false otherwise.


class TreeNode:
    def __init__(self):
        self.children = [None] * 26 # english alphabet
        self.end = False

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def _map_char_to_int(self, c):
        return ord(c.lower()) - ord('a') 

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            indx = self._map_char_to_int(letter)
            if node.children[indx] is None:
                node.children[indx] = TreeNode()
            node = node.children[indx]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            indx = self._map_char_to_int(letter)
            if node.children[indx] is None:
                return False
            node = node.children[indx]
        return node.end

        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            indx = self._map_char_to_int(letter)
            if node.children[indx] is None:
                return False
            node = node.children[indx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)