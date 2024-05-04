# 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA)
# of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def _naive_dfs(self, root, p, q):

        path_p, path_q = None, None
        queue = deque([ (root, [] ) ])
        while queue:
            node, path = queue.popleft()

            if node is not None:
                new_path = path + [node]

                if node == p:
                    path_p = new_path
                if node == q:
                    path_q = new_path

                if path_q is not None and path_p is not None:
                    break

                queue.appendleft( (node.right, new_path) )
                queue.appendleft( (node.left, new_path) )
        
        min_len = min(len(path_p), len(path_q))
        c = 0
        for i,j in zip(path_p[:min_len], path_q[:min_len]):
            if i == j:
                c+=1
            else:
                break
        
        return path_p[c-1]

    def _smarter_recursive_LCA(self, root, p, q):
        """Solution devised from @priyanshu11_"""

        # base cases
        if not root or root == p or root == q:
            return root

        left = self._smarter_recursive_LCA(root.left, p, q)
        right = self._smarter_recursive_LCA(root.right, p, q)


        if left and right:
            # this means p and q are on different subtrees
            # ie. the root is the lowest ancestor
            return root

        elif left:
            return left
        
        else:
            return right
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self._smarter_recursive_LCA(root, p, q)
        