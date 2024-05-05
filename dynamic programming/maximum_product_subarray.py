# 152. Maximum Product Subarray
# Given an integer array nums, find a subarray
# that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # we should keep max and minimum, because if we have a negative number
        # the minimum will become maximum and vice versa
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            
            # max is maximum between the number itself, 
            # number*max, or number*min (incase number<0)
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)

            # min so far is minimum between the number itself,
            # number*max (incase number<0), or number*min (incase number>0)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max
            if max_so_far > result:
                result = max_so_far

        return result