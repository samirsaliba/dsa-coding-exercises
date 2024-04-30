# 746. Min Cost Climbing Stairs
# You are given an integer array cost where 
# cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

class Solution:
    def _min_cost_to(self, x):
        if x == 0:
            return self._cost[0]
        elif x == 1:
            return self._cost[1]
        
        elif x in self._cache:
            return self._cache[x]
        
        cost_x_minus_1 = self._min_cost_to(x-1) + self._cost[x]
        cost_x_minus_2 = self._min_cost_to(x-2) + self._cost[x]
        cost_x = min(cost_x_minus_1, cost_x_minus_2)
        self._cache[x] = cost_x
        return cost_x
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if cost is None:
            return cost

        self._cache = {}
        self._cost = cost
        return min(self._min_cost_to(len(cost)-1), self._min_cost_to(len(cost)-2)) 
