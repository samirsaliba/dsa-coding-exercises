# 1268. Search Suggestions System
# You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names 
# from products after each character of searchWord is typed. 
# Suggested products should have common prefix with searchWord. 
# If there are more than three products with a common prefix 
# return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of searchWord is typed.


"""
NOTE: While this solution works, I'm not super proud of it as I know it could
be way more efficient. Indexing the children backwards and 
that "reversed" call are tricks I found to make it functional 
but are definitely not the ideal.
I'll give it more thought and figure something more efficient soon
"""
from collections import deque
class TreeNode():
    def __init__(self, val=None):
        self.children = [None] * 26
        self.end = False
        self.val = val

class Trie():
    def __init__(self):
        self.root = TreeNode()

    def _char_to_index(self, c):
        return 25 - ( ord(c.lower()) - ord('a') ) # indexing backwards

    def insert(self, word):
        node = self.root
        for i, letter in enumerate(word):
            indx = self._char_to_index(letter)
            if node.children[indx] is None:
                node.children[indx] = TreeNode()
            node = node.children[indx]
        node.val = word
        node.end = True

    def _dfs(self, node, include_node_word=False):
        queue = deque(reversed(node.children))
        words = []
        if include_node_word:
            words.append(node.val)
        while queue:
            node = queue.popleft()
            if node is not None:
                queue.extendleft(node.children)
                if node.end == True:
                    words.append(node.val)
                    if len(words) == 3:
                        return words
        return words

    def search_prefix(self, prefix):
        node = self.root
        for letter in prefix:
            indx = self._char_to_index(letter)
            if node.children[indx] is None:
                return []
            node = node.children[indx]
        return self._dfs(node, include_node_word=node.end)
            
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tree = Trie()
        for product in products:
            tree.insert(product)

        words = []
        i=1
        while i < len(searchWord)+1:
            words.append(tree.search_prefix(searchWord[:i]))
            i+=1

        return words

        