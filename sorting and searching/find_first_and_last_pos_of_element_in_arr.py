# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search_occurr(self, nums, target, search_start_pos):
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = left + (right-left)//2

            if nums[mid] > target:
                # num must be left of mid
                right = mid-1
            
            elif nums[mid] < target:
                # num must be right of mid
                left = mid+1

            else:
                # found num, but we must keep looking for either first/last
                if search_start_pos:
                    if left == mid  or nums[mid-1] < target:
                        # found lower bound
                        return mid
                    
                    # else keep searching left for first occurrence
                    right = mid-1
                
                else:
                    # looking for end position
                    if right == mid or nums[mid+1] > target:
                        # found end
                        return mid
                    
                    # else we keep searching right for the last occurrence
                    left = mid+1
        
        return -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_pos = self.search_occurr(nums, target, search_start_pos=True)
        if start_pos == -1:
            return [-1, -1]

        end_pos = self.search_occurr(nums, target, search_start_pos=False)
        
        return [start_pos, end_pos]


