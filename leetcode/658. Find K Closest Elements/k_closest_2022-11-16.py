#!/usr/bin/env python3
"""https://leetcode.com/problems/find-k-closest-elements/"""

class Solution:
    def findClosestElements(self, nums: list[int], k: int, target: int) -> list[int]:
        l, r = 0, len(nums) - k - 1
        while l <= r:
            m = (l + r) // 2
            if target - nums[m] > nums[m + k] - target:
                l = m + 1
            else:
                r = m - 1
        k_closest = nums[l:l + k]
        return k_closest
