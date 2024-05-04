# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences 
# of each value in the array is unique or false otherwise.

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurr = {}
        for n in arr:
            occurr[n] = occurr.get(n, 0) + 1

        return len(occurr) == len(set(occurr.values()))