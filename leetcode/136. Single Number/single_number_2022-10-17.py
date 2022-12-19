#!/usr/bin/env python3
"""https://leetcode.com/problems/single-number/"""

from functools import reduce
import operator


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x


class SolutionAlternate:
    def singleNumber(self, nums: list[int]) -> int:
        x = reduce(operator.xor, nums)
        return x


class SolutionAlternate2:
    def singleNumber(self, nums: list[int]) -> int:
        sum_set = sum(set(nums))
        sum_actual = sum(nums)
        return 2 * sum_set - sum_actual
