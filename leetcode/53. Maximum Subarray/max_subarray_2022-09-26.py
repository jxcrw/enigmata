#!/usr/bin/env python3
"""https://leetcode.com/problems/maximum-subarray/"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum_max, sum_temp = -float('inf'), 0
        for num in nums:
            sum_temp = max(sum_temp + num, num)
            sum_max = max(sum_max, sum_temp)
        return sum_max
