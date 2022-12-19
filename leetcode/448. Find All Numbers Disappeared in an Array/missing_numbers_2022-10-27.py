#!/usr/bin/env python3
"""https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/"""


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            i_target = abs(num) - 1
            if nums[i_target] > 0:
                nums[i_target] *= -1

        missing = [i + 1 for i, num in enumerate(nums) if num > 0]
        return missing


class SolutionAlternate:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seen, n = set(nums), len(nums)
        missing = [i for i in range(1, n + 1) if i not in seen]
        return missing


class SolutionAlternate2:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        self._cyclic_sort(nums)
        missing = [i + 1 for i, num in enumerate(nums) if i + 1 != num]
        return missing

    def _cyclic_sort(self, nums: list[int]) -> None:
        i, n = 0, len(nums)
        while i < n:
            i_target = nums[i] - 1
            if nums[i_target] != nums[i]:
                nums[i_target], nums[i] = nums[i], nums[i_target]
            else:
                i += 1
