# 63. Unique Paths II
# You are given an m x n integer array grid. There is a robot initially
# located at the top-left corner (i.e., grid[0][0]). The robot tries to
# move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. 
# A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to 
# reach the bottom-right corner.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [ [0] * n for _ in range(m)]

        # since we can only move down or right
        # we can initialize the top row and left column
        for row in range(m):
            if obstacleGrid[row][0] == 0:
                grid[row][0] = 1
            else:
                break # found obstacle in row
        
        for col in range(n):
            if obstacleGrid[0][col] == 0:
                grid[0][col] = 1
            else:
                break # found obstacle in col
        
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 0: # no obstacle
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]
        
        return grid[m-1][n-1]