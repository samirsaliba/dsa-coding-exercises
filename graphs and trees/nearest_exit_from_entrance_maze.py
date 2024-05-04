# 1926. Nearest Exit from Entrance in Maze
# You are given an m x n matrix maze (0-indexed) 
# with empty cells (represented as '.') 
# and walls (represented as '+'). 
# You are also given the entrance of the maze, where
# entrance = [entrancerow, entrancecol] denotes the row and column 
# of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. 
# You cannot step into a cell with a wall, 
# and you cannot step outside the maze. 
# Your goal is to find the nearest exit from the entrance. 
# An exit is defined as an empty cell that is at the border of the maze. 
# The entrance does not count as an exit.

# Return the number of steps in the shortest path
# from the entrance to the nearest exit, or -1 if no such path exists.

from collections import deque

class Solution:
    def _is_border(self, i, j):
        return not ((0<i<self.m-1) and (0<j<self.n-1))

    def _consider_move(self, moves, i, j, steps):
        if self.maze[i][j] == '.' and ((i,j) not in self.visited): 
            self.visited.add((i,j))
            moves.append([i,j,steps])

    def _possible_moves(self, row, col, steps):
        moves = []
        steps += 1

        if self.m > 1:
            if row > 0:
                # up (inverted)
                i, j = row-1, col
                self._consider_move(moves, i, j, steps)

            if row < self.m-1:
                # down
                i, j = row+1, col
                self._consider_move(moves, i, j, steps)


        if self.n > 1:
            if col < self.n-1:
                # right
                i, j = row, col+1
                self._consider_move(moves, i, j, steps)

            if col > 0:
                # left            
                i, j = row, col-1
                self._consider_move(moves, i, j, steps)

        return moves

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.m, self.n = len(maze), len(maze[0])
        self.maze = maze
        i, j = entrance
        self.visited = {(i,j)}
        q = deque(self._possible_moves(i, j, steps=0))

        while q:
            i, j, steps = q.popleft()
            if self._is_border(i,j):
                # found exit
                return steps
            
            q.extend(self._possible_moves(i, j, steps))

        return -1


            
        
        