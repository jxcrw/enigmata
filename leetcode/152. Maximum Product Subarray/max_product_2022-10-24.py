#!/usr/bin/env python3
"""https://leetcode.com/problems/maximum-product-subarray/"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_temp, max_temp, max_final = 1, 1, -float('inf')
        for num in nums:
            x = min_temp * num
            y = max_temp * num
            min_temp = min(num, x, y)
            max_temp = max(num, x, y)
            max_final = max(max_final, min_temp, max_temp)
        return max_final
