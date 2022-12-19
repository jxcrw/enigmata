#!/usr/bin/env python3
"""https://leetcode.com/problems/kth-missing-positive-number/"""

class Solution:
    def findKthPositive(self, nums: list[int], k: int) -> int:
        missing_as_of = lambda i: nums[i] - i - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if missing_as_of(m) < k: l = m + 1
            else: r = m - 1
        missing = nums[r] + k - missing_as_of(r)
        return missing
