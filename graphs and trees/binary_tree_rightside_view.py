# 199. Binary Tree Right Side View
# Given the root of a binary tree,
# imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
from typing import List, Optional
class Solution:
    def _dfs_rightest(self, root):
        queue = deque([root])
        levels = deque([0])
        max_level = -1
        visible = []
        while queue:
            node = queue.popleft()
            level = levels.popleft()

            if node is not None:
                if level > max_level:
                    max_level = level
                    visible.append(node.val)

                for lr in [node.left, node.right]:
                    queue.appendleft(lr)
                    levels.appendleft(level+1)
                
        return visible


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        return self._dfs_rightest(root)