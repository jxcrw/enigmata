#!/usr/bin/env python3
"""https://leetcode.com/problems/sort-characters-by-frequency/"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c_freqs = Counter(s)
        max_freq = max(c_freqs.values())

        buckets = [[] for _ in range(max_freq + 1)]
        for c, freq in c_freqs.items():
            buckets[freq].append(c)

        builder = []
        for i in reversed(range(len(buckets))):
            for c in buckets[i]:
                builder.append(c * i)

        s_sorted = ''.join(builder)
        return s_sorted


class SolutionAlt:
    def frequencySort(self, s: str) -> str:
        c_freqs = Counter(s)
        builder = [c * freq for c, freq in c_freqs.most_common()]
        s_sorted = ''.join(builder)
        return s_sorted
