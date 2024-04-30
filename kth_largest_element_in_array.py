# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, 
# return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.
# Can you solve it without sorting?

from collections import deque

class MinHeap():
    def __init__(self, n):
        self._n = deque(n)
        self._construct_heap()

    def _min_heapify(self, i):
        # heapifies a node
        left = 2*i
        right = (2*i) + 1
        smaller_node = i

        if left < len(self._n) and self._n[left] < self._n[i]:
            smaller_node = left

        if right < len(self._n) and self._n[right] < self._n[smaller_node]:
            smaller_node = right

        if smaller_node != i:
            aux = self._n[i]
            self._n[i] = self._n[smaller_node]
            self._n[smaller_node] = aux
            self._min_heapify(smaller_node)

    def _construct_heap(self):
        # we construct heap from the bottom going up, heapifying
        # the nodes along the way
        # we dont heapify the leaf nodes - they already satisfy heap
        # condition since they have no children
        m = len(self._n)
        for i in range(m // 2, -1, -1):
            self._min_heapify(i)

    def pop(self):
        el = self._n.popleft()
        self._min_heapify(0)
        return el
    
    def push(self, x):
        self._n.appendleft(x)
        self._min_heapify(0)


class Solution:

    def _slower(self, nums, k):
        # own implementation is accepted but slower

        if not nums:
            return nums

        heap = MinHeap(nums[:k])
        for num in nums[k:]:
            if num > heap._n[0]:
                heap.pop()
                heap.push(num)
        return heap._n[0]

    def _faster(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]


    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return nums
        return self._faster(nums, k)
