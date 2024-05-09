# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Solution logic: Using prefix sum
# If the cumulative sum up to two indices is the same, the sum of the
# elements lying in between those indices is zero. Extending the same
# thought further, if the cumulative sum up to two indices, say i and j
# is at a difference of k i.e. if sum[i]−sum[j]=k, 
# the sum of elements lying between indices i and j is k.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        sum_freq = dict()
        
        for num in nums:
            curr_sum += num

            if curr_sum == k:
                # this happens when the first contiguous array sums to k
                count += 1

            # if the frequency of index (curr_sum-k) is > 0
            # that means the array between the current num (ie. i)
            # and (curr_sum-k) (ie. j) sums to k
            count += sum_freq.get(curr_sum - k, 0)

            # Add +1 to the frequency of the current sum
            sum_freq[curr_sum] = 1 + sum_freq.get(curr_sum, 0)

        return count