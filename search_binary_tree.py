# 700. Search in a Binary Search Tree

# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val 
# and return the subtree rooted with that node. 
# If such a node does not exist, return null.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return root
        node = root
        while node is not None:
            if val > node.val:
                    node = node.right
            elif val < node.val:
                    node = node.left
            else:
                return node
        return None
        