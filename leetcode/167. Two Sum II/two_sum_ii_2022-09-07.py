#!/usr/bin/env python3
"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total < target: l += 1
            elif total > target: r -= 1
            else: return [l + 1, r + 1]
        return []
