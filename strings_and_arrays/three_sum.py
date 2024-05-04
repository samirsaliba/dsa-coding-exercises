# 15. 3Sum
# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                # if nums[i] eqls the previous one, no need to re-do
                # the calculations
                continue

            j, k = i+1, len(nums)-1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]

                if three_sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j+=1

                    while nums[j] == nums[j-1] and j<k:
                        # repeated matches should be ignored
                        j+=1
                
                elif three_sum > 0:
                    k-=1
                
                else:
                    j+=1
    
        return triplets
            

        