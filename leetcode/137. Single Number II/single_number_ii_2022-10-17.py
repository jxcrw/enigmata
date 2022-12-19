#!/usr/bin/env python3
"""https://leetcode.com/problems/single-number-ii/"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once
