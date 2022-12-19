#!/usr/bin/env python3
"""https://leetcode.com/problems/peak-index-in-a-mountain-array/"""

class Solution:
    def peakIndexInMountainArray(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1
        return l
