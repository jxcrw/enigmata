#!/usr/bin/env python3
"""https://leetcode.com/problems/first-missing-positive/"""

import timeit


class SolutionInitial:
    # Time / Space: O(|nums|) / O(max(nums))
    def firstMissingPositive(self, nums: list[int]) -> int:
        max_num = max(nums) if max(nums) > 0 else 1
        seen = set(nums)
        for i in range(1, max_num + 2):
            if i not in seen:
                return i
        return -1


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        self._cyclic_sort(nums)
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1

    def _cyclic_sort(self, nums: list[int]):
        i, n = 0, len(nums)
        while i < n:
            i_target = nums[i] - 1
            if 0 <= i_target < n and nums[i_target] != nums[i]:
                nums[i_target], nums[i] = nums[i], nums[i_target]
            else:
                i += 1


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 3)
    nums = [1, 2, 0]
    print(s_init.firstMissingPositive(nums))
    print(s_pref.firstMissingPositive(nums))

    # Example 2 (Expected Output: 2)
    nums = [3, 4, -1, 1]
    print(s_init.firstMissingPositive(nums))
    print(s_pref.firstMissingPositive(nums))

    # Example 3 (Expected Output: 1)
    nums = [7, 8, 9, 11, 12]
    print(s_init.firstMissingPositive(nums))
    print(s_pref.firstMissingPositive(nums))

    # Benchmarking
    number = 10_000
    nums = list(range(500)) + list(range(501, 1000))
    print(timeit.timeit(lambda: s_init.firstMissingPositive(nums), number=number))
    print(timeit.timeit(lambda: s_pref.firstMissingPositive(nums), number=number))
