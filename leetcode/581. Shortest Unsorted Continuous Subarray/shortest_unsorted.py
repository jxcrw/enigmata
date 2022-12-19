#!/usr/bin/env python3
"""https://leetcode.com/problems/shortest-unsorted-continuous-subarray/"""

import timeit


class Solution:
    # Time / Space: O(n) / O(1)
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        r = 0
        max_seen = -float('inf')
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                r = i

        l = 0
        min_seen = float('inf')
        for i in reversed(range(n)):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                l = i

        return r - l + 1 if r > 0 else 0


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: 5)
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(solution.findUnsortedSubarray(nums))

    # Example 2 (Expected Output: 0)
    nums = [1, 2, 3, 4]
    print(solution.findUnsortedSubarray(nums))

    # Example 3 (Expected Output: 0)
    nums = [1]
    print(solution.findUnsortedSubarray(nums))

    # Benchmarking
    number = 10_000
    nums = [1]
    print(timeit.timeit(lambda: solution.findUnsortedSubarray(nums), number=number))
