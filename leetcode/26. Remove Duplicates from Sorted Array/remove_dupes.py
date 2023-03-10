#!/usr/bin/env python3
"""https://leetcode.com/problems/remove-duplicates-from-sorted-array/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n), O(1)
    def removeDuplicates(self, nums: list[int]) -> int:
        l = r = 0
        while r < len(nums):
            val = nums[r]
            while r < len(nums) and nums[r] == val: r += 1
            nums[l] = val
            l += 1
        return l

class SolutionPreferred:
    # Time / Space: O(n), O(1)
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l + 1


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 2, [1, 2, _])
    nums = [1, 1, 2]
    nums2 = nums[:]
    print(s_init.removeDuplicates(nums))
    print(s_pref.removeDuplicates(nums2))

    # Example 2 (Expected Output: 5, [0, 1, 2, 3, 4, _, _, _, _, _])
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums2 = nums[:]
    print(s_init.removeDuplicates(nums))
    print(s_pref.removeDuplicates(nums2))

    # Benchmarking
    number = 10_000
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums2 = nums[:]
    print(timeit.timeit(lambda: s_init.removeDuplicates(nums), number=number))
    print(timeit.timeit(lambda: s_pref.removeDuplicates(nums2), number=number))
