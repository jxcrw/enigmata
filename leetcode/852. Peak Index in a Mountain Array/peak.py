#!/usr/bin/env python3
"""https://leetcode.com/problems/peak-index-in-a-mountain-array/"""

import timeit


class SolutionInitial:
    # Time / Space: O(log n) / O(1)
    def peakIndexInMountainArray(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            on_peak = nums[m - 1] < nums[m] > nums[m + 1]
            is_ascending = nums[m] < nums[m + 1]

            if on_peak: return m
            elif is_ascending: l = m + 1
            else: r = m - 1
        return -1


class SolutionPreferred:
    # Time / Space: O(log n) / O(1)
    def peakIndexInMountainArray(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            is_ascending = nums[m] < nums[m + 1]
            if is_ascending: l = m + 1
            else: r = m - 1
        return l


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 0 (Expected Output: 1)
    nums = [0, 1, 0]
    print(s_init.peakIndexInMountainArray(nums))
    print(s_pref.peakIndexInMountainArray(nums))

    # Example 1 (Expected Output: 1)
    nums = [0, 2, 1, 0]
    print(s_init.peakIndexInMountainArray(nums))
    print(s_pref.peakIndexInMountainArray(nums))

    # Example 2 (Expected Output: 1)
    nums = [0, 10, 5, 2]
    print(s_init.peakIndexInMountainArray(nums))
    print(s_pref.peakIndexInMountainArray(nums))

    # Example 3 (Expected Output: 5)
    nums = [0, 1, 2, 3, 4, 10, 9, 8, 7, 6, 2]
    print(s_init.peakIndexInMountainArray(nums))
    print(s_pref.peakIndexInMountainArray(nums))

    # Benchmarking
    number = 10_000
    nums = list(range(100_000_000)) + [10_000_000] + list(reversed(range(10_000_000)))
    print(timeit.timeit(lambda: s_init.peakIndexInMountainArray(nums), number=number))
    print(timeit.timeit(lambda: s_pref.peakIndexInMountainArray(nums), number=number))
