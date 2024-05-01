# 994. Rotting Oranges
# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent
# to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse 
# until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque

class Solution:
    def _check_adjacent(self, adj, i, j, minute):
        if self.grid[i][j] == 1:
            # this fresh orange will be rotten in next minute
            self.fresh -= 1
            self.grid[i][j] = 2
            adj.append((i,j,minute))

    def _adjacent_fresh_oranges(self, i, j, minute):
        minute += 1
        adjacent = []
        if self.m > 1:
            if i > 0:
                self._check_adjacent(adjacent, i-1, j, minute) # up (inv.)

            if i < self.m-1: 
                self._check_adjacent(adjacent, i+1, j, minute) # down

        if self.n > 1:
            if j > 0: 
                self._check_adjacent(adjacent, i, j-1, minute) # left

            if j < self.n-1:
                self._check_adjacent(adjacent, i, j+1, minute) # right

        return adjacent

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0]) 
        self.grid = grid
        q = deque()
        
        # check for starting oranges that are rotten and counting fresh
        self.fresh = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j,0))

        max_minutes = 0
        while q:
            i, j, minute = q.popleft()
            max_minutes = max(max_minutes, minute)
            adj_fresh = self._adjacent_fresh_oranges(i, j, minute)
            q.extend(adj_fresh)
        
        if self.fresh == 0:
            return max_minutes
        return -1
