#!/usr/bin/env python3
"""https://leetcode.com/problems/single-number-iii/"""

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        diff = bitmask & -bitmask

        x = 0
        for num in nums:
            if num & diff:
                x ^= num
        y = bitmask ^ x

        return [x, y]
