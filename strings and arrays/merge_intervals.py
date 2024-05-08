# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by starting time
        intervals = sorted(intervals, key= lambda x:x[0]) 
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                # if the ith interval ends after the start of the i+1th
                # that means they can be merged
                # the new interval end is the max of the two intervals endings
                interval_end = max(intervals[i][1], intervals[i+1][1])
                new_interval = [intervals[i][0], interval_end]
                intervals[i] = new_interval
                del intervals[i+1]
            else:
                i+=1
                
        return intervals