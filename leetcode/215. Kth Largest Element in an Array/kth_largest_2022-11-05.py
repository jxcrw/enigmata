#!/usr/bin/env python3
"""https://leetcode.com/problems/kth-largest-element-in-an-array/"""

from heapq import heappop, heappush, nlargest
from random import randint


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        def partition(l: int, r: int, p: int) -> int:
            pivot = nums[p]
            nums[p], nums[r] = nums[r], nums[p]

            i_swap = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[i_swap] = nums[i_swap], nums[i]
                    i_swap += 1

            nums[r], nums[i_swap] = nums[i_swap], nums[r]
            return i_swap

        def quickselect(l: int, r: int, k: int) -> int:
            if l == r: return nums[l]

            p = randint(l, r)
            p = partition(l, r, p)

            if k == p:
                return nums[k]
            elif k < p:
                return quickselect(l, p - 1, k)
            else:
                return quickselect(p + 1, r, k)

        n = len(nums)
        kth_largest = quickselect(0, n - 1, n - k)
        return kth_largest


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = []
        for num in nums:
            heappush(h, num)
            if len(h) > k:
                heappop(h)
        return h[0]

    def findKthLargest2(self, nums: list[int], k: int) -> int:
        kth_largest = nlargest(k, nums)[-1]
        return kth_largest
