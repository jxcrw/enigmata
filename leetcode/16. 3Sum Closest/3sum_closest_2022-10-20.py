#!/usr/bin/env python3
"""https://leetcode.com/problems/3sum-closest/"""

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        diff_min, n = float('inf'), len(nums)
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum < target: l += 1
                else: r -= 1

                diff = target - threesum
                if diff == 0: return threesum
                if abs(diff) < abs(diff_min):
                    diff_min = diff
                    sum_closest = threesum

        return sum_closest
