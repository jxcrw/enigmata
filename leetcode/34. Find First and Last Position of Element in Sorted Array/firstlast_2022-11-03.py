#!/usr/bin/env python3
"""https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"""

from bisect import bisect_left


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self._bisect_left(nums, target)
        right = self._bisect_left(nums, target + 1) - 1
        was_found = left <= right
        return [left, right] if was_found else [-1, -1]

    def _bisect_left(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l


class SolutionAlt:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = bisect_left(nums, target)
        right = bisect_left(nums, target + 1) - 1
        was_found = left <= right
        return [left, right] if was_found else [-1, -1]
