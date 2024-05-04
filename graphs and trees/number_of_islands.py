# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map 
# of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.


from collections import deque

class Solution:
    def _adj(self, point):
        adj_list = []
        i,j = point

        if i>0:
            # up
            if self.grid[i-1][j] == "1": adj_list.append((i-1, j))

        if i < self.m-1:
            # down
            if self.grid[i+1][j] == "1": adj_list.append((i+1, j))
        
        if j>0:
            # left
            if self.grid[i][j-1] == "1": adj_list.append((i, j-1))

        if j<self.n-1:
            # right
            if self.grid[i][j+1] == "1": adj_list.append((i, j+1))

        return adj_list

    def _dfs(self, start):
        q = deque([start])
        while q:
            point = q.popleft()
            if point not in self.visited:
                q.extendleft(self._adj(point))
                self.visited.add(point)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m, self.n = len(grid), len(grid[0]) 
        self.grid = grid
        land_points = []
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    land_points.append((i,j))

        islands = 0
        self.visited = set()
        for point in land_points:
            if point not in self.visited:
                self._dfs(point)
                islands += 1
                if len(self.visited) == len(land_points):
                    break #early stopping

        return islands

