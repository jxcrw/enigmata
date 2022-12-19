#!/usr/bin/env python3
"""https://leetcode.com/problems/missing-number/"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        seen, n = set(nums), len(nums)
        for i in range(n + 1):
            if i not in seen:
                return i


class SolutionAlternate:
    def missingNumber(self, nums: list[int]) -> int:
        self._cyclic_sort(nums)
        for i, num in enumerate(nums):
            if i != num: return i
        return len(nums)

    def _cyclic_sort(self, nums: list[int]):
        i, n = 0, len(nums)
        while i < n:
            i_target = nums[i]
            if i_target < n and i_target != i:
                nums[i_target], nums[i] = nums[i], nums[i_target]
            else:
                i += 1


class SolutionAlternate2:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum_expected = n * (n + 1) // 2
        sum_actual = sum(nums)
        missing = sum_expected - sum_actual
        return missing
