#!/usr/bin/env python3
"""https://leetcode.com/problems/find-all-duplicates-in-an-array/"""

import timeit


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def findDuplicates(self, nums: list[int]) -> list[int]:
        dupes = []
        for num in nums:
            num_abs = abs(num)
            target_index = num_abs - 1
            if nums[target_index] > 0:
                nums[target_index] *= -1
            else:
                dupes.append(num_abs)
        return dupes


class SolutionAlternate:
    # Time / Space: O(n) / O(1)
    def findDuplicates(self, nums: list[int]) -> list[int]:
        self._cyclic_sort(nums)
        dupes = [num for i, num in enumerate(nums) if i + 1 != num]
        return dupes

    def _cyclic_sort(self, nums: list[int]):
        i, n = 0, len(nums)
        while i < n:
            i_target = nums[i] - 1
            if nums[i_target] != nums[i]:
                nums[i_target], nums[i] = nums[i], nums[i_target]
            else:
                i += 1


class SolutionAlternate2:
    # Time / Space: O(n) / O(n)
    def findDuplicates(self, nums: list[int]) -> list[int]:
        dupes, seen = [], set()
        for num in nums:
            if num in seen: dupes.append(num)
            seen.add(num)
        return dupes


if __name__ == '__main__':
    s_pref = SolutionPreferred()
    s_alt = SolutionAlternate()
    s_alt2 = SolutionAlternate2()

    # Example 1 (Expected Output: [2, 3])
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s_pref.findDuplicates(nums[:]))
    print(s_alt.findDuplicates(nums[:]))
    print(s_alt2.findDuplicates(nums[:]))

    # Example 2 (Expected Output: [1])
    nums = [1, 1, 2]
    print(s_pref.findDuplicates(nums[:]))
    print(s_alt.findDuplicates(nums[:]))
    print(s_alt2.findDuplicates(nums[:]))

    # Example 3 (Expected Output: [])
    nums = [1]
    print(s_pref.findDuplicates(nums[:]))
    print(s_alt.findDuplicates(nums[:]))
    print(s_alt2.findDuplicates(nums[:]))

    # Benchmarking
    number = 1_000
    nums = list(range(1, 10000)) + [151]
    print(timeit.timeit(lambda: s_pref.findDuplicates(nums[:]), number=number))
    print(timeit.timeit(lambda: s_alt.findDuplicates(nums[:]), number=number))
    print(timeit.timeit(lambda: s_alt2.findDuplicates(nums[:]), number=number))
