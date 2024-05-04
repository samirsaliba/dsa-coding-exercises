# 2336. Smallest Number in Infinite Set
# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object
# to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained
# in the infinite set.
# void addBack(int num) Adds a positive integer num back into 
# the infinite set, if it is not already in the infinite set.

import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self._heap = list(range(1, 1001))
        self._popped_nums = set()
        
    def popSmallest(self) -> int:
        x = heapq.heappop(self._heap)
        self._popped_nums.add(x)
        return x
    
    def addBack(self, num: int) -> None:
        if num in self._popped_nums:
            # number has been previously popped off
            # so we should insert it back
            heapq.heappush(self._heap, num)
            self._popped_nums.remove(num)
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)