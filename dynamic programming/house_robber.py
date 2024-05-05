# 198. House Robber
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have
# security systems connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can use dynamic programming to solve this problem, bottom-up
        # we can define the profit[i] as the maximum profit that can be made
        # by robbing the first i houses
        # then, for i+1, we can either rob the ith house or not
        # if we rob the ith house, we can only rob the i-2th house
        # if we don't rob the ith house, we can rob the i-1th house

        if len(nums) == 1:
            return nums[0]

        profit_0 = nums[0]
        profit_1 = max(nums[0], nums[1])
        profit = [profit_0, profit_1]

        for i in range(2, len(nums)):
            max_i = max(
                profit[i-2] + nums[i], # rob the current one
                profit[i-1] # rob the previous one
            )
            profit.append(max_i)

        return profit[-1]