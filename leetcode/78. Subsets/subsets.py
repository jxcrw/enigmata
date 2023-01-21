#!/usr/bin/env python3
"""https://leetcode.com/problems/subsets/"""

import itertools

from tools.lc_tools import benchmark, init_solutions, pretty_eval


class SolutionInit:
    # Time / Space: O(n * 2^n) /  O(n * 2^n)
    def subsets(self, nums: list[int]) -> list[list[int]]:
        powerset = []
        n = len(nums)

        for bitmask in itertools.product('01', repeat=n):
            subset = [nums[i] for i in range(n) if bitmask[i] == '1']
            powerset.append(subset)

        return powerset


class SolutionPref:
    # Time / Space: O(n * 2^n) /  O(n * 2^n)
    def subsets(self, nums: list[int]) -> list[list[int]]:
        powerset = [[]]

        for num in nums:
            powerset += [subset + [num] for subset in powerset]

        return powerset


if __name__ == '__main__':
    # Setup
    solutions = init_solutions(globals())
    method = 'subsets'

    # Examples
    inputs = [[1, 2, 3], [0]]
    outputs = [[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], [[], [0]]]
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 250
    args = list(range(10))
    benchmark(solutions, method, args, number)
