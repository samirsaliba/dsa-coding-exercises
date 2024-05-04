# 1161. Maximum Level Sum of a Binary Tree
# Given the root of a binary tree, the level of its root is 1, 
# the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values 
# of nodes at level x is maximal.

from collections import deque
from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _bfs_sum(self, root):
        level_sums = [None] * 1000
        queue = deque([root])
        levels = deque([0])
        while queue:
            node = queue.popleft()
            level = levels.popleft()

            if node is not None:
                curr_sum = level_sums[level]
                if curr_sum is not None: 
                    level_sums[level] = curr_sum + node.val
                else:
                    level_sums[level] = node.val
                queue.extend([node.left, node.right])
                levels.extend([level+1] * 2)
                
        level = 1
        max_sum = level_sums[0]
        for i, val in enumerate(level_sums, start=1):
            if val is None:
                break
            elif val>max_sum:
                level=i
                max_sum=val
        return level
    
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return None
        return self._bfs_sum(root)