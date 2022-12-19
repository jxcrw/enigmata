#!/usr/bin/env python3
"""https://leetcode.com/problems/subarray-product-less-than-k/"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0
        count, product = 0, 1
        l = 0
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                product /= nums[l]
                l += 1
            count += r - l + 1
        return count
