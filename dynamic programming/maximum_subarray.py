# 53. Maximum Subarray
# Given an integer array nums, find the 
# subarray with the largest sum, and return its sum.

"""
Note: I've left the (left, right) pointers commented out
as they are not required for this problem.
However, if you want to return the subarray, you can just use them
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # left, right = None, None
        max_sum = -1 * float('inf')
        
        window_sum = -1 * float('inf')
        # window_left, window_right = None, None

        for i in range(n):
            # window pointer always right
            # window_right = i

            if window_sum > 0:
                # window sum positive, keep extending window
                window_sum += nums[i]

            else:
                # window sum <= 0, means new window starts here
                # window_left = i
                window_sum = nums[i]

            if window_sum > max_sum:
                # best window so far
                max_sum = window_sum
                # left = window_left
                # right = window_right

        return max_sum