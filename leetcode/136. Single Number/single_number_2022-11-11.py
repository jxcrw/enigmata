#!/usr/bin/env python3
"""https://leetcode.com/problems/single-number/"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x


class SolutionAlt:
    def singleNumber(self, nums: list[int]) -> int:
        sum_set = sum(set(nums))
        sum_actual = sum(nums)
        single = 2 * sum_set - sum_actual
        return single
