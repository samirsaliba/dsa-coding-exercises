# 210. Course Schedule II
# There are a total of numCourses courses you have to take, 
# labeled from 0 to numCourses - 1. You are given an array prerequisites 
# where prerequisites[i] = [ai, bi] indicates that you must take course bi first
# if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0
# you have to first take course 1.
# Return the ordering of courses you should take to finish all courses.
# If there are many valid answers,
# return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    # 0 is white -- ie. not seen
    # 1 is gray -- ie. evaluating its adj
    # 2 is black -- ie. node closed

    WHITE = 0
    GRAY = 1
    BLACK = 2

    def _dfs(self, node):
        if self.cycle == True:
            return

        self.color[node] = Solution.GRAY # gray
        for adj in self.graph[node]:
            adj_color = self.color[adj]

            if adj_color == 0:
                # if adj is white, go-to adj
                self._dfs(adj)

            elif adj_color == Solution.GRAY:
                # found an open node, this means a cycle
                self.cycle = True
                return

            # else case would be color=Black
            # but nothing to be done

        # recursion ends, meaning we have visited all adj
        # must close the node, ie color=Black
        self.color[node] = Solution.BLACK
        self.visited_order.append(node)
                
            
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.graph = defaultdict(list)
        
        for ai, bi in prerequisites:
            # if we need b to do a
            # then edge is b -> a
            self.graph[bi].append(ai)

        self.color = {
            k: Solution.WHITE for k in range(numCourses)
        }
        self.visited_order = []
        self.cycle = False

        for vertex in range(numCourses):
            if self.color[vertex] == Solution.WHITE:
                self._dfs(vertex)
                if self.cycle:
                    return []
        
        return self.visited_order[::-1]
            
            
            