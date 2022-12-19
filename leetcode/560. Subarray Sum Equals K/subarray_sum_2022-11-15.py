#!/usr/bin/env python3
"""https://leetcode.com/problems/subarray-sum-equals-k/"""

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = prefix_sum = 0
        sum_counts = defaultdict(int, {0: 1})

        for num in nums:
            prefix_sum += num

            diff = prefix_sum - k
            count += sum_counts.get(diff, 0)

            sum_counts[prefix_sum] += 1

        return count
