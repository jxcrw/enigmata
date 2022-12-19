#!/usr/bin/env python3
"""https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/"""

from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, nums: list[int], k: int) -> int:
        num_freqs = Counter(nums)
        freq_max = max(num_freqs.values())

        buckets = [[] for _ in range(freq_max + 1)]
        for num, freq in num_freqs.items():
            buckets[freq].append(num)

        for freq in range(len(buckets)):
            if k < freq: break
            bucket = buckets[freq]
            while bucket and k >= freq:
                del num_freqs[bucket.pop()]
                k -= freq

        return len(num_freqs)
