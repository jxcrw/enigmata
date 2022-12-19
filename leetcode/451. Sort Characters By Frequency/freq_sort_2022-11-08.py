#!/usr/bin/env python3
"""https://leetcode.com/problems/sort-characters-by-frequency/"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        char_freqs = Counter(s)
        freq_max = max(char_freqs.values())

        buckets = [[] for _ in range(freq_max + 1)]
        for c, f in char_freqs.items():
            buckets[f].append(c)

        builder = []
        for f in reversed(range(len(buckets))):
            for c in buckets[f]:
                builder.append(c * f)

        s_sorted = ''.join(builder)
        return s_sorted


class SolutionAlt:
    def frequencySort(self, s: str) -> str:
        char_freqs = Counter(s)
        builder = [c * f for c, f in char_freqs.most_common()]
        s_sorted = ''.join(builder)
        return s_sorted
