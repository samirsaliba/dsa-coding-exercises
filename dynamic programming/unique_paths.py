# 62. Unique Paths
# There is a robot on an m x n grid. The robot is initially located at
# the top-left corner (i.e., grid[0][0]). The robot tries to move to the
#  bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # considering robot can only move down and right
        # theres only one path for going through
        # the top row or the left column
        # so we can start the values as 1
        # and skip them in the loop - they are base cases

        grid = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                # to get to ij, we can only come from the above or the left
                # neighbors, so we just sum their respective paths
                grid[row][col] = grid[row-1][col] + grid[row][col-1]

        # last element is the target
        return grid[m-1][n-1]
