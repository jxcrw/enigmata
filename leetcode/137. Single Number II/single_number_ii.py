#!/usr/bin/env python3
"""https://leetcode.com/problems/single-number-ii/"""

import timeit


class Solution:
    # Time / Space: O(n) / O(1)
    def singleNumber(self, nums: list[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: 3)
    nums = [2, 2, 3, 2]
    print(solution.singleNumber(nums))

    # Example 2 (Expected Output: 99)
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(solution.singleNumber(nums))

    # Benchmarking
    number = 10_000
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(timeit.timeit(lambda: solution.singleNumber(nums), number=number))
