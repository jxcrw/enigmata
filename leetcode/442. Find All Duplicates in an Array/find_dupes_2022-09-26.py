#!/usr/bin/env python3
"""https://leetcode.com/problems/find-all-duplicates-in-an-array/"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        dupes = []
        for num in nums:
            num_abs = abs(num)
            target_index = num_abs - 1
            if nums[target_index] > 0:
                nums[target_index] *= -1
            else:
                dupes.append(num_abs)
        return dupes


class SolutionAlternate:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        self._cyclic_sort(nums)
        dupes = [num for i, num in enumerate(nums) if i + 1 != num]
        return dupes

    def _cyclic_sort(self, nums: list[int]):
        i, n = 0, len(nums)
        while i < n:
            i_target = nums[i] - 1
            if nums[i_target] != nums[i]:
                nums[i_target], nums[i] = nums[i], nums[i_target]
            else:
                i += 1
