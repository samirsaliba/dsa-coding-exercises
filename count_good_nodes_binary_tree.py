# 1448. Count Good Nodes in Binary Tree
# Given a binary tree root, a node X in the tree is named good if
# in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _dfs_good_node(self, root):
        # queue will keep the node and max_value in path so far
        q = deque([(root, root.val-1)])
        good_nodes = 0

        while q:
            node, max_in_path = q.popleft()
            if node:
                if node.val >=  max_in_path:
                    # node is good
                    good_nodes += 1
                    max_in_path = node.val

                q.appendleft((node.right, max_in_path))
                q.appendleft((node.left, max_in_path))
        
        return good_nodes


    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return root
        return self._dfs_good_node(root)
        