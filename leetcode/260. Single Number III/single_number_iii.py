#!/usr/bin/env python3
"""https://leetcode.com/problems/single-number-iii/"""

from collections import Counter
import timeit


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def singleNumber(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        missing = [x for x in counter if counter[x] == 1]
        return missing


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def singleNumber(self, nums: list[int]) -> list[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        diff = bitmask & -bitmask

        x = 0
        for num in nums:
            if num & diff:
                x ^= num
        y = bitmask ^ x

        return [x, y]


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [3, 5])
    nums = [1, 2, 1, 3, 2, 5]
    print(s_init.singleNumber(nums))
    print(s_pref.singleNumber(nums))

    # Example 2 (Expected Output: [-1, 0])
    nums = [-1, 0]
    print(s_init.singleNumber(nums))
    print(s_pref.singleNumber(nums))

    # Example 3 (Expected Output: [1, 0])
    nums = [0, 1]
    print(s_init.singleNumber(nums))
    print(s_pref.singleNumber(nums))

    # Benchmarking
    number = 10_000
    nums = list(range(1000)) + [990, 991]
    print(timeit.timeit(lambda: s_init.singleNumber(nums), number=number))
    print(timeit.timeit(lambda: s_pref.singleNumber(nums), number=number))
