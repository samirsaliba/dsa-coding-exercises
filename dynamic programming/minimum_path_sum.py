# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right, 
# which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sum_grid = [ [0] * n for _ in range(m)]

        # since we can only move either down or right
        # first row and first column are just a consecutive sum of them

        curr_sum = 0
        for row in range(m):
            curr_sum += grid[row][0]
            sum_grid[row][0] = curr_sum
            
        curr_sum = 0
        for col in range(n):
            curr_sum += grid[0][col]
            sum_grid[0][col] = curr_sum
            
        for row in range(1, m):
            for col in range(1, n):
                coming_right = sum_grid[row-1][col]
                coming_down = sum_grid[row][col-1]
                best = min(coming_right, coming_down)
                sum_grid[row][col] = best + grid[row][col]

        # bottom right is last element
        return sum_grid[m-1][n-1]
        