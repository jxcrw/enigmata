#!/usr/bin/env python3
"""https://leetcode.com/problems/missing-number/"""

import random
import timeit


class SolutionTimsort:
    # Time / Space: O(n log n) / O(n)
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num: return i
        return len(nums)


class SolutionHashset:
    # Time / Space: O(n) / O(n)
    def missingNumber(self, nums: list[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in num_set:
                return i


class SolutionBitbanger:
    # Time / Space: O(n) / O(1)
    def missingNumber(self, nums: list[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


class SolutionMath:
    # Time / Space: O(n) / O(1)
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum_expected = n * (n + 1) // 2
        sum_actual = sum(nums)
        return sum_expected - sum_actual


class SolutionCyclicSort:
    # Time / Space: O(n) / O(1)
    def missingNumber(self, nums: list[int]) -> int:
        self._cyclic_sort(nums)
        for i, num in enumerate(nums):
            if i != num: return i
        return len(nums)

    def _cyclic_sort(self, nums: list[int]):
        i, n = 0, len(nums)
        while i < n:
            i_target = nums[i]
            if i_target < n and i_target != i:
                nums[i_target], nums[i] = nums[i], nums[i_target]
            else:
                i += 1


if __name__ == '__main__':
    s_timsort = SolutionTimsort()
    s_hashset = SolutionHashset()
    s_bitbanger = SolutionBitbanger()
    s_math = SolutionMath()
    s_cyclicsort = SolutionCyclicSort()

    # Example 1 (Expected Output: 2)
    nums = [3, 0, 1]
    print(s_timsort.missingNumber(nums[:]))
    print(s_hashset.missingNumber(nums[:]))
    print(s_bitbanger.missingNumber(nums[:]))
    print(s_math.missingNumber(nums[:]))
    print(s_cyclicsort.missingNumber(nums[:]))

    # Example 2 (Expected Output: 2)
    nums = [0, 1]
    print(s_timsort.missingNumber(nums[:]))
    print(s_hashset.missingNumber(nums[:]))
    print(s_bitbanger.missingNumber(nums[:]))
    print(s_math.missingNumber(nums[:]))
    print(s_cyclicsort.missingNumber(nums[:]))

    # Example 3 (Expected Output: 8)
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(s_timsort.missingNumber(nums[:]))
    print(s_hashset.missingNumber(nums[:]))
    print(s_bitbanger.missingNumber(nums[:]))
    print(s_math.missingNumber(nums[:]))
    print(s_cyclicsort.missingNumber(nums[:]))

    # Benchmarking
    number = 5_000
    nums = list(range(number))
    nums.remove(number // 2)
    random.shuffle(nums)

    print(timeit.timeit(lambda: s_timsort.missingNumber(nums[:]), number=number))    # baseline
    print(timeit.timeit(lambda: s_hashset.missingNumber(nums[:]), number=number))  # baseline/2
    print(timeit.timeit(lambda: s_bitbanger.missingNumber(nums[:]), number=number)) # ≈baseline
    print(timeit.timeit(lambda: s_math.missingNumber(nums[:]), number=number)) # FAST!!!
    print(timeit.timeit(lambda: s_cyclicsort.missingNumber(nums[:]), number=number))  # 2x baseline
