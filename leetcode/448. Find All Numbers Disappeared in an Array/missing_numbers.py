#!/usr/bin/env python3
"""https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/"""

import random
import timeit


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seen, n = set(nums), len(nums)
        missing = [i for i in range(1, n + 1) if i not in seen]
        return missing


class SolutionAlternate:
    # Time / Space: O(n) / O(1)
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        self._cyclic_sort(nums)
        missing = [i + 1 for i, num in enumerate(nums) if i + 1 != num]
        return missing

    def _cyclic_sort(self, nums: list[int]):
        i, n = 0, len(nums)
        while i < n:
            i_target = nums[i] - 1
            if nums[i_target] != nums[i]:
                nums[i_target], nums[i] = nums[i], nums[i_target]
            else:
                i += 1


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            target_index = abs(num) - 1
            if nums[target_index] > 0:
                nums[target_index] *= -1

        missing = [i + 1 for i, num in enumerate(nums) if num > 0]
        return missing


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [5, 6])
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s_init.findDisappearedNumbers(nums[:]))
    print(s_alt.findDisappearedNumbers(nums[:]))
    print(s_pref.findDisappearedNumbers(nums[:]))

    # Example 2 (Expected Output: [2])
    nums = [1, 1]
    print(s_init.findDisappearedNumbers(nums[:]))
    print(s_alt.findDisappearedNumbers(nums[:]))
    print(s_pref.findDisappearedNumbers(nums[:]))

    # Benchmarking
    number = 3_000
    nums = list(range(number))
    nums[number // 2] = number - 1
    random.shuffle(nums)

    print(timeit.timeit(lambda: s_init.findDisappearedNumbers(nums[:]), number=number))
    print(timeit.timeit(lambda: s_alt.findDisappearedNumbers(nums[:]), number=number))
    print(timeit.timeit(lambda: s_pref.findDisappearedNumbers(nums[:]), number=number))
