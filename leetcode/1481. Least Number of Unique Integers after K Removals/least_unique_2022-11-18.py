#!/usr/bin/env python3
"""https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/"""

from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, nums: list[int], k: int) -> int:
        num_freqs = Counter(nums)
        freq_max = max(num_freqs.values())

        buckets = [[] for _ in range(freq_max + 1)]
        for n, f in num_freqs.items():
            buckets[f].append(n)

        for f in range(len(buckets)):
            if k < f: break
            bucket = buckets[f]
            while bucket and k >= f:
                del num_freqs[bucket.pop()]
                k -= f

        return len(num_freqs)
