#!/usr/bin/env python3
"""https://leetcode.com/problems/shortest-unsorted-continuous-subarray/"""

class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        r = 0
        max_seen = -float('inf')
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                r = i

        l = 0
        min_seen = float('inf')
        for i in reversed(range(n)):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                l = i

        return r - l + 1 if r > 0 else 0
