#!/usr/bin/env python3
"""https://leetcode.com/problems/subarray-sum-equals-k/"""

from collections import defaultdict
import timeit


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def subarraySum(self, nums: list[int], target: int) -> int:
        count = prefix_sum = 0
        sum_counts = defaultdict(int)

        for num in nums:
            prefix_sum += num
            if prefix_sum == target: count += 1

            diff = prefix_sum - target
            count += sum_counts.get(diff, 0)

            sum_counts[prefix_sum] += 1
        return count


class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def subarraySum(self, nums: list[int], target: int) -> int:
        count = prefix_sum = 0
        sum_counts = defaultdict(int, {0: 1})

        for num in nums:
            prefix_sum += num

            diff = prefix_sum - target
            count += sum_counts.get(diff, 0)

            sum_counts[prefix_sum] += 1
        return count


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 2)
    nums, target = [1, 1, 1], 2
    print(s_init.subarraySum(nums, target))
    print(s_pref.subarraySum(nums, target))

    # Example 2 (Expected Output: 2)
    nums, target = [1, 2, 3], 3
    print(s_init.subarraySum(nums, target))
    print(s_pref.subarraySum(nums, target))

    # Benchmarking
    number = 1000
    nums, target = list(range(10_000)), 500
    print(timeit.timeit(lambda: s_init.subarraySum(nums, target), number=number))
    print(timeit.timeit(lambda: s_pref.subarraySum(nums, target), number=number))
