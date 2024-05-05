# 410. Split Array Largest Sum
# Given an integer array nums and an integer k, 
# split nums into k non-empty subarrays such that
# the largest sum of any subarray is minimized.
# Return the minimized largest sum of the split.
# A subarray is a contiguous part of the array.

class Solution:

    def _split_array_dp(self, curr_index, k):
        
        if (curr_index,k) in self.cache:
            return self.cache[(curr_index,k)]
        
        # no splits left, return sum of the rest of the elements
        if k == 1:
            return self.prefix_sum[self.n] - self.prefix_sum[curr_index]


        # starting min_max as the largest possible
        min_largest_split_sum = self.prefix_sum[self.n]

        for j in range(curr_index, self.n - k + 1):

            sum_first = self.prefix_sum[j+1] - self.prefix_sum[curr_index]
            sum_rest = self._split_array_dp(j+1, k-1)
            largest_split_sum = max(sum_first, sum_rest)

            if largest_split_sum < min_largest_split_sum:
                # found new min_largest, update
                min_largest_split_sum = largest_split_sum 

            if sum_first >= min_largest_split_sum:
                # first array is already too big, 
                # different splits of the remaining elements won't help
                break

        self.cache[(curr_index,k)] = min_largest_split_sum
        return min_largest_split_sum

    def splitArray(self, nums: List[int], k: int) -> int:
        self.cache = {}
        self.n = len(nums)
        self.prefix_sum = [0]
        for i in range(1, self.n+1):
            psum = self.prefix_sum[i-1] + nums[i-1]
            self.prefix_sum.append(psum)

        print(self.prefix_sum)

        return self._split_array_dp(curr_index=0, k=k)

