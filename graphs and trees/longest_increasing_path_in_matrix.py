# 329. Longest Increasing Path in a Matrix
# Given an m x n integers matrix, return the length 
# of the longest increasing path in matrix.
# From each cell, you can either move in four directions:
# left, right, up, or down. You may not move diagonally 
# or move outside the boundary (i.e., wrap-around is not allowed).

# Solution:
# We can do a DFS search for each cell
# and cache the longest path for each cell (i,j) along the way
# since most of the searches will explore the same cells

class Solution:
    def _moves(self, ij):
        i, j = ij
        moves = []
        val = self.matrix[i][j]

        if i > 0:
            # up
            if val < self.matrix[i-1][j]:
                moves.append((i-1, j))
        
        if i < self.m - 1:
            # down
            if val < self.matrix[i+1][j]:
                moves.append((i+1, j))
        
        if j > 0:
            # left
            if val < self.matrix[i][j-1]:
                moves.append((i, j-1))

        if j < self.n - 1:
            # left
            if val < self.matrix[i][j+1]:
                moves.append((i, j+1))

        return moves
    
    def _dfs(self, ij):
        if ij in self.cache:
            return self.cache[ij]

        sub_paths_len = [self._dfs(move) for move in self._moves(ij)]

        if len(sub_paths_len) > 0:
            res = 1 + max(sub_paths_len)
            self.cache[ij] = res
            return res

        self.cache[ij] = 1 
        return 1            

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
        self.cache = {}
        
        max_len = 0
        for i in range(self.m):
            for j in range(self.n):
                maxlen_ij = self._dfs((i,j))
                if maxlen_ij > max_len:
                    max_len = maxlen_ij
        
        return max_len
        