# 547. Number of Provinces
# There are n cities. Some of them are connected, while some are not. 
# If city a is connected directly with city b, 
# and city b is connected directly with city c, 
# then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities 
# and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 
# if the ith city and the jth city are directly connected, 
# and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

from collections import deque
class Solution:
    def _dfs(self, start, M):
        visited = set()
        q = deque([start])

        while q:
            city_a = q.popleft()
            visited.add(city_a)
            for city_b, connected in enumerate(M[city_a]):
                if connected == 1 and city_b not in visited:
                    q.appendleft(city_b)

        return visited


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = list(range(len(isConnected)))
        provinces = 0
        visited = set()
        for city in cities:
            if city not in visited:
                visited_from_city = self._dfs(city, isConnected)
                visited.update(visited_from_city)
                provinces+=1
            
                if visited == set(cities):
                    break

        return provinces