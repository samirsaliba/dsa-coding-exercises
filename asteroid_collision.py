# 735. Asteroid Collision
# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, 
# and the sign represents its direction 
# (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. 
# If two asteroids meet, the smaller one will explode. 
# If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.

from collections import deque

class Solution:
    def _en_collision_route(self, prev, ast):
        both_positive = ast>0 and prev>0
        both_negative = ast<0 and prev<0

        if not (both_positive or both_negative) and prev > 0:
            return True

        return False


    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = deque([asteroids[0]])

        for ast in asteroids[1:]:
            if not q:
                q.append(ast)
                continue

            prev = q.pop()
            while self._en_collision_route(prev, ast):
                if abs(ast) > abs(prev):
                    if q:
                        prev = q.pop() # explodes prev
                    
                    else:
                        q.append(ast)
                        break

                elif abs(ast) < abs(prev):
                    q.append(prev)
                    break
                else:
                    break # eql

            if not self._en_collision_route(prev, ast):
                q.append(prev)
                q.append(ast)

        return q
        