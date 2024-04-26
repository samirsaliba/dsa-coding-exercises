"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque 

class Solution:
    def _naive_solution(self, node):
        new_head = Node(val=node.val)
        visited = {new_head.val: new_head}
        discovered = set(node.neighbors)

        while discovered:
            new = discovered.pop()            
            new_node = Node(val=new.val)
            visited[new.val] = new_node
            for neigh in new.neighbors:
                if neigh.val in visited:
                    new_node.neighbors.append(visited[neigh.val])
                    visited[neigh.val].neighbors.append(new_node)
                else:
                    discovered.add(neigh)
            
        return new_head

    def _deque_solution(self, node):
        clones = {node.val: Node(val=node.val)}
        queue = deque([node])

        while queue:
            new = queue.popleft()
            new_clone = clones[new.val]

            for neigh in new.neighbors:
                if neigh.val not in clones:
                    clones[neigh.val] = Node(neigh.val)
                    queue.append(neigh)

                new_clone.neighbors.append(clones[neigh.val])
        return clones[node.val]

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        return self._deque_solution(node)