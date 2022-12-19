#!/usr/bin/env python3
"""https://leetcode.com/problems/missing-number/"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        seen = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in seen:
                return i


class SolutionAlternate:
    def missingNumber(self, nums: list[int]) -> int:
        self._cyclic_sort(nums)
        for i, n in enumerate(nums):
            if i != n: return i
        return len(nums)

    def _cyclic_sort(self, nums: list[int]):
        i, n = 0, len(nums)
        while i < n:
            num = nums[i]
            if num < n and num != i:
                nums[i], nums[num] = nums[num], nums[i]
            else:
                i += 1


class SolutionAlternate2:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum_expected = n * (n + 1) // 2
        sum_actual = sum(nums)
        return sum_expected - sum_actual
