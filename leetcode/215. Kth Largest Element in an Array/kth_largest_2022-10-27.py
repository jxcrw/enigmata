#!/usr/bin/env python3
"""https://leetcode.com/problems/kth-largest-element-in-an-array/"""

from heapq import heappop, heappush, nlargest
import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.findKthSmallest(nums, len(nums) - k + 1)

    def findKthSmallest(self, nums: list[int], k: int) -> int:
        if not nums: return 0

        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthSmallest(left, k)
        elif k <= L + M:
            return pivot
        else:
            return self.findKthSmallest(right, k - M - L)


class SolutionAlternate:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

    def findKthLargest2(self, nums: list[int], k: int) -> int:
        kth_largest = nlargest(k, nums)[-1]
        return kth_largest
