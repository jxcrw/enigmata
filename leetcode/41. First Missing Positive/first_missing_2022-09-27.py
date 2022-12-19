#!/usr/bin/env python3
"""https://leetcode.com/problems/first-missing-positive/"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        self._cyclic_sort(nums)
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1

    def _cyclic_sort(self, nums: list[int]):
        i, n = 0, len(nums)
        while i < n:
            i_target = nums[i] - 1
            if 0 <= i_target < n and nums[i_target] != nums[i]:
                nums[i_target], nums[i] = nums[i], nums[i_target]
            else:
                i += 1
