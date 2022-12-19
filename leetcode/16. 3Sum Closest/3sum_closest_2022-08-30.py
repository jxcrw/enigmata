#!/usr/bin/env python3
"""https://leetcode.com/problems/3sum-closest/"""

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n, diff_min = len(nums), float('inf')
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                sum_temp = nums[i] + nums[l] + nums[r]
                if sum_temp < target: l += 1
                else: r -= 1

                diff = target - sum_temp
                if diff == 0: return sum_temp
                if abs(diff) < abs(diff_min):
                    diff_min = diff
                    sum_closest = sum_temp

        return sum_closest
