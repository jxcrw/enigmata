#!/usr/bin/env python3
"""https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1 or nums[l] < nums[r]: return nums[l]

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]: return nums[m + 1]
            elif nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        return -1
