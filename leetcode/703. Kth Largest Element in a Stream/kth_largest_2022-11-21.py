#!/usr/bin/env python3
"""https://leetcode.com/problems/kth-largest-element-in-a-stream/"""

from heapq import heappop, heappush


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        k, h = self.k, self.heap
        heappush(h, val)
        if len(h) > k:
            heappop(h)
        return h[0]
