# 57. Insert Interval
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end
# of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end]
# that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted
# in ascending order by starti and intervals still does not have any 
# overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

import bisect 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        # O(logn) search but insertion is still O(n)
        bisect.insort_left(intervals, newInterval, key=lambda x:x[0])

        # merge intervals
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                start = intervals[i][0]
                end = max(intervals[i][1], intervals[i+1][1])
                intervals[i] = [start, end]
                del intervals[i+1]
            else:
                i+=1

        return intervals