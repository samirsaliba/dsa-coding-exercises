# 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        queue = deque([root])
        depth = {root: 1}

        while queue:
            node = queue.popleft()
            node_depth = depth[node]
            for child_node in [node.left, node.right]:
                if child_node is not None:
                    depth[child_node] = node_depth + 1
                    queue.appendleft(child_node)
            
        return max(depth.values())

        