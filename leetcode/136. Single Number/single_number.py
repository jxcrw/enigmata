#!/usr/bin/env python3
"""https://leetcode.com/problems/single-number/"""

from collections import defaultdict
import timeit


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def singleNumber(self, nums: list[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        for num in counts:
            if counts[num] == 1:
                return num


class SolutionAlternate:
    # Time / Space: O(n) / O(1)
    def singleNumber(self, nums: list[int]) -> int:
        sum_set = sum(set(nums))
        sum_actual = sum(nums)
        return 2 * sum_set - sum_actual


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def singleNumber(self, nums: list[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 1)
    nums = [2, 2, 1]
    print(s_init.singleNumber(nums))
    print(s_alt.singleNumber(nums))
    print(s_pref.singleNumber(nums))

    # Example 2 (Expected Output: 4)
    nums = [4, 1, 2, 1, 2]
    print(s_init.singleNumber(nums))
    print(s_alt.singleNumber(nums))
    print(s_pref.singleNumber(nums))

    # Example 3 (Expected Output: 1)
    nums = [1]
    print(s_init.singleNumber(nums))
    print(s_alt.singleNumber(nums))
    print(s_pref.singleNumber(nums))

    # Benchmarking
    number = 2_000
    nums = [0] * number + [1]
    print(timeit.timeit(lambda: s_init.singleNumber(nums), number=number))
    print(timeit.timeit(lambda: s_alt.singleNumber(nums), number=number))
    print(timeit.timeit(lambda: s_pref.singleNumber(nums), number=number))
