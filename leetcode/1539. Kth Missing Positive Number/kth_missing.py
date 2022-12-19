#!/usr/bin/env python3
"""https://leetcode.com/problems/kth-missing-positive-number/"""

import timeit


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def findKthPositive(self, nums: list[int], k: int) -> int:
        seen = set(nums)
        missing = [i for i in range(1, k + len(nums) + 1) if i not in seen]
        kth_missing = missing[k - 1]
        return kth_missing


class SolutionAlternate:
    # Time / Space: O(n) / O(n)
    def findKthPositive(self, nums: list[int], k: int) -> int:
        seen = set(nums)
        for i in range(1, k + len(nums) + 1):
            if i not in seen: k -= 1
            if k == 0: return i


class SolutionPreferred:
    # Time / Space: O(log n) / O(1)
    def findKthPositive(self, nums: list[int], k: int) -> int:
        missing_as_of = lambda i: nums[i] - i - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if missing_as_of(m) < k:
                l = m + 1
            else:
                r = m - 1
        return nums[r] + k - missing_as_of(r)


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 9)
    nums, k = [2, 3, 4, 7, 11], 5
    print(s_init.findKthPositive(nums, k))
    print(s_pref.findKthPositive(nums, k))

    # Example 2 (Expected Output: 6)
    nums, k = [1, 2, 3, 4], 2
    print(s_init.findKthPositive(nums, k))
    print(s_pref.findKthPositive(nums, k))

    # Benchmarking
    number = 10_000
    nums, k = list(range(1000)), 2
    print(timeit.timeit(lambda: s_init.findKthPositive(nums, k), number=number))
    print(timeit.timeit(lambda: s_pref.findKthPositive(nums, k), number=number))
