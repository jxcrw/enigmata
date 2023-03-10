#!/usr/bin/env python3
"""https://leetcode.com/problems/max-consecutive-ones-iii/"""

from collections import defaultdict
import timeit

class SolutionInitial:
    # Time / Space: O(n) / O(1)
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = count_0s = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count_0s += 1
            if count_0s > k:
                if nums[l] == 0: count_0s -= 1
                l += 1
        return r - l + 1

class SolutionAlternate:
    # Time / Space: O(n) / O(1)
    def longestOnes(self, nums: list[int], k: int) -> int:
        l, counts = 0, defaultdict(int)
        for r in range(len(nums)):
            counts[nums[r]] += 1
            if counts[0] > k:
                counts[nums[l]] -= 1
                l += 1
        return r - l + 1

class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            k -= 1 - nums[r]
            if k < 0:
                k += 1 - nums[l]
                l += 1
        return r - l + 1


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 6)
    nums, k = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2
    print(s_init.longestOnes(nums, k))
    print(s_alt.longestOnes(nums, k))
    print(s_pref.longestOnes(nums, k))

    # Example 2 (Expected Output: 10)
    nums, k = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    print(s_init.longestOnes(nums, k))
    print(s_alt.longestOnes(nums, k))
    print(s_pref.longestOnes(nums, k))

    # Benchmarking
    number = 10_000
    nums, k = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    print(timeit.timeit(lambda: s_init.longestOnes(nums, k), number=number))
    print(timeit.timeit(lambda: s_alt.longestOnes(nums, k), number=number))
    print(timeit.timeit(lambda: s_pref.longestOnes(nums, k), number=number))
