# 1493. Longest Subarray of 1's After Deleting One Element
# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray 
# containing only 1's in the resulting array.
# Return 0 if there is no such subarray.

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        streak = 0
        max_streak = 0
        max_streak_start = 0
        curr_streak_start = -1
        block_i = -1
        blocked = False

        i = 0
        while i<len(nums):
            if nums[i] == 1:
                if streak == 0:
                    # starting streak
                    curr_streak_start = i
                streak += 1

            else:
                # found 0
                if not blocked:
                    if streak > 0:
                        # found zero in nonzero seq
                        blocked = True
                        block_i = i

                else:
                    # found second zero in seq
                    # that means end of previous seq
                    # should reset streak and pointers
                    if streak > max_streak:
                        # if it's best seq so far
                        max_streak = streak
                        max_streak_start = curr_streak_start

                    streak = 0 
                    i = block_i # going back to previous first block
                    blocked = False
            i+=1

        # accounting for the last streak
        if streak > max_streak:
            max_streak = streak
            max_streak_start = curr_streak_start

        if block_i == -1:
            # edge case when no 0s found between 1s
            if curr_streak_start == -1:
                # no ones found at all
                return 0
            elif curr_streak_start == 0:
                # no zeroes found at all
                return max_streak - 1

        # happy case
        return max_streak

        