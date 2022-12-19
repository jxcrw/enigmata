#!/usr/bin/env python3
"""https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"""

from bisect import bisect_left


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = self._bisect_left(nums, target)
        end = self._bisect_left(nums, target + 1) - 1
        was_found = start <= end
        return [start, end] if was_found else [-1, -1]

    def _bisect_left(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l


class SolutionAlternate:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = bisect_left(nums, target)
        end = bisect_left(nums, target + 1) - 1
        was_found = start <= end
        return [start, end] if was_found else [-1, -1]
