#!/usr/bin/env python3
"""https://leetcode.com/problems/find-all-duplicates-in-an-array/"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        dupes = []
        for num in nums:
            num_abs = abs(num)
            i_target = num_abs - 1
            if nums[i_target] > 0:
                nums[i_target] *= -1
            else:
                dupes.append(num_abs)
        return dupes


class SolutionAlt:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        self._cyclic_sort(nums)
        dupes = [num for i, num in enumerate(nums) if num != i + 1]
        return dupes

    def _cyclic_sort(self, nums: list[int]) -> None:
        i, n = 0, len(nums)
        while i < n:
            i_target = nums[i] - 1
            if nums[i_target] != nums[i]:
                nums[i_target], nums[i] = nums[i], nums[i_target]
            else:
                i += 1
