#!/usr/bin/env python3
"""https://leetcode.com/problems/4sum/"""

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        return self._ksum(nums, target, k=4)

    def _ksum(self, nums: list[int], target: int, k: int) -> list[list[int]]:
        res = []
        if not nums: return res

        average = target // k
        if average < nums[0] or average > nums[-1]: return res

        if k == 2: return self._twosum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                for subset in self._ksum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)

        return res

    def _twosum(self, nums: list[int], target: int) -> list[list[int]]:
        res, n = [], len(nums)
        l, r = 0, n - 1
        while l < r:
            twosum = nums[l] + nums[r]
            if twosum < target or (l > 0 and nums[l] == nums[l - 1]):
                l += 1
            elif twosum > target or (r < n - 1 and nums[r] == nums[r + 1]):
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
        return res
