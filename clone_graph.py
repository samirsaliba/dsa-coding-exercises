# 133. Clone Graph
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). 
# For example, the first node with val == 1, the second node with val == 2, and so on. 
# The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. 
# You must return the copy of the given node as a reference to the cloned graph.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
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

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        return self._naive_solution(node)