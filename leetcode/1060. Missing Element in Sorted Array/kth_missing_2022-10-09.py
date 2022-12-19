#!/usr/bin/env python3
"""https://leetcode.com/problems/missing-element-in-sorted-array/"""

class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        missing_as_of = lambda i: nums[i] - i - nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if missing_as_of(m) < k:
                l = m + 1
            else:
                r = m - 1
        return nums[r] - missing_as_of(r) + k
