# Given the root of a binary tree, 
# return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path 
# between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented 
# by the number of edges between them.

class Solution:
    max_dist = 0

    def max_len_dfs(self, node):
        if node is None:
            return 0
        
        len_right = self.max_len_dfs(node.right)
        len_left = self.max_len_dfs(node.left)

        dist_node = len_left + len_right
        if dist_node > self.max_dist:
            self.max_dist = dist_node

        return max(len_right, len_left) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _ = self.max_len_dfs(root)
        return self.max_dist
        