class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """Derived from adityawdubey"""
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-2] < nums[-1]:
            return len(nums)-1


        # i, j hold start and beginning of the array we're searching
        # since we have already checked first and last elements
        i = 1
        j = len(nums) - 2

        while i <= j:
            mid = i + (j-i) // 2

            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid+1] > nums[mid]:
                # right is greater, search right
                i = mid + 1

            else:
                # left is greater, search left
                j = mid - 1

        return None
        