# 1268. Search Suggestions System
# You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names 
# from products after each character of searchWord is typed. 
# Suggested products should have common prefix with searchWord. 
# If there are more than three products with a common prefix 
# return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of searchWord is typed.


"""
NOTE: Not the best but better
"""

from typing import List

class TreeNode():
    def __init__(self, val=None):
        self.children = [None] * 26
        self.end = False
        self.val = val

def _char_to_index(c):
    return ord(c.lower()) - ord('a')


class Trie():
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        node = self.root
        for i, letter in enumerate(word):
            indx = _char_to_index(letter)
            if node.children[indx] is None:
                node.children[indx] = TreeNode(letter)
            node = node.children[indx]
        node.end = True
        
class Solution:
    def _search_prefix(self, root, prefix):
        node = root
        for letter in prefix:
            indx = _char_to_index(letter)
            if node.children[indx] is None:
                return []
            node = node.children[indx]
        return self._dfs(node, start_prefix=prefix)

    def _dfs(self, node, start_prefix):
        if node is None: return []
        if node in self._cache:
            return self._cache[node]

        words = []
        if node.end == True: 
            words.append(start_prefix)
        for child in node.children:
            if child is not None:
                words.extend(self._dfs(child, start_prefix=start_prefix + child.val))
                if len(words) > 3: 
                    break
        self._cache[node] = words[0:3]
        return words[0:3]
        

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tree = Trie()
        for product in products:
            tree.insert(product)

        self._cache = {}
        words = []
        i=1
        while i < len(searchWord)+1:
            words.append(self._search_prefix(tree.root, searchWord[:i]))
            i+=1

        return words

        