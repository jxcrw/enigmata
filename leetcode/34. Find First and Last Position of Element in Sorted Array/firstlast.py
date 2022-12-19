#!/usr/bin/env python3
"""https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"""

from bisect import bisect_left
import timeit


class SolutionInitial:
    # Time / Space: O(log n) / O(1)
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = bisect_left(nums, target)
        right = bisect_left(nums, target + 1) - 1
        was_found = left <= right
        return [left, right] if was_found else [-1, -1]


class SolutionPreferred:
    # Time / Space: O(log n) / O(1)
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self._bisect_left(nums, target)
        right = self._bisect_left(nums, target + 1) - 1
        was_found = left <= right
        return [left, right] if was_found else [-1, -1]

    def _bisect_left(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 0 (Expected Output: [3, 4])
    nums, target = [5, 7, 7, 8, 8, 8, 10], 8
    print(s_init.searchRange(nums, target))
    print(s_pref.searchRange(nums, target))

    # Example 1 (Expected Output: [-1, -1])
    nums, target = [5, 7, 7, 8, 8, 10], 6
    print(s_init.searchRange(nums, target))
    print(s_pref.searchRange(nums, target))

    # Example 2 (Expected Output: [-1, -1])
    nums, target = [], 0
    print(s_init.searchRange(nums, target))
    print(s_pref.searchRange(nums, target))

    # Example 3 (Expected Output: [0, 0])
    nums, target = [1], 1
    print(s_init.searchRange(nums, target))
    print(s_pref.searchRange(nums, target))

    # Benchmarking
    number = 10_000
    nums, target = list(range(10_000_000)), 5_000_000
    print(timeit.timeit(lambda: s_init.searchRange(nums, target), number=number))
    print(timeit.timeit(lambda: s_pref.searchRange(nums, target), number=number))
