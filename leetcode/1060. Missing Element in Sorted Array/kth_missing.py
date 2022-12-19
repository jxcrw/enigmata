#!/usr/bin/env python3
"""https://leetcode.com/problems/missing-element-in-sorted-array/"""

import timeit


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def missingElement(self, nums: list[int], k: int) -> int:
        seen, start = set(nums), nums[0]
        for i in range(start, start + k + len(nums) + 1):
            if i not in seen:
                k -= 1
            if k == 0:
                return i


class SolutionPreferred:
    # Time / Space: O(log n) / O(1)
    def missingElement(self, nums: list[int], k: int) -> int:
        missing_as_of = lambda i: nums[i] - i - nums[0]
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

    # Example 1 (Expected Output: 5)
    nums, k = [4, 7, 9, 10], 1
    print(s_init.missingElement(nums, k))
    print(s_pref.missingElement(nums, k))

    # Example 2 (Expected Output: 8)
    nums, k = [4, 7, 9, 10], 3
    print(s_init.missingElement(nums, k))
    print(s_pref.missingElement(nums, k))

    # Example 3 (Expected Output: 6)
    nums, k = [1, 2, 4], 3
    print(s_init.missingElement(nums, k))
    print(s_pref.missingElement(nums, k))

    # Benchmarking
    number = 10_000
    nums, k = list(range(1000)), 2
    print(timeit.timeit(lambda: s_init.missingElement(nums, k), number=number))
    print(timeit.timeit(lambda: s_pref.missingElement(nums, k), number=number))
