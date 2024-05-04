# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed
# to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time 
# and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] 
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])

        # using nums as output list
        last_value = nums[-1]
        last_suffix = 1
        nums[-1] = prefix[-1]

        for i in range(len(nums)-2, -1, -1):
            last_suffix = last_suffix * last_value
            last_value = nums[i]
            nums[i] = last_suffix * prefix[i]
        
        return nums

