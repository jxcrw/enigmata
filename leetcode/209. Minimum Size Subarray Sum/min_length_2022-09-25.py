#!/usr/bin/env python3
"""https://leetcode.com/problems/minimum-size-subarray-sum/"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        length_min, total = n + 1, 0

        l = 0
        for r in range(n):
            total += nums[r]
            while total >= target:
                length_min = min(length_min, r - l + 1)
                total -= nums[l]
                l += 1
        return length_min if length_min <= n else 0
