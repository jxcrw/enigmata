#!/usr/bin/env python3
"""https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/"""

from collections import Counter

from tools.lc_tools import benchmark, init_solutions, pretty_eval


class SolutionInit:
    # Time / Space: O(n log n) / O(n)
    def findLeastNumOfUniqueInts(self, nums: list[int], k: int) -> int:
        num_freqs = Counter(nums)
        for num, freq in reversed(num_freqs.most_common()):
            if k >= freq:
                k -= freq
                num_freqs.pop(num)
            else:
                break
        return len(num_freqs)


class SolutionPref:
    # Time / Space: O(n) / O(n)
    def findLeastNumOfUniqueInts(self, nums: list[int], k: int) -> int:
        num_freqs = Counter(nums)
        max_freq = max(num_freqs.values())

        buckets = [[] for _ in range(max_freq + 1)]
        for num, freq in num_freqs.items():
            buckets[freq].append(num)

        for freq in range(len(buckets)):
            if k < freq: break

            bucket = buckets[freq]
            while bucket and k >= freq:
                del num_freqs[bucket.pop()]
                k -= freq

        return len(num_freqs)


if __name__ == '__main__':
    # Setup
    solutions = init_solutions(globals())
    method = 'findLeastNumOfUniqueInts'

    # Examples
    inputs = [([5, 5, 4], 1), ([4, 3, 1, 1, 3, 3, 2], 3)]
    outputs = [1, 2, 2]
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 250
    args = (list(range(20_000)), 10_000)
    benchmark(solutions, method, args, number)
