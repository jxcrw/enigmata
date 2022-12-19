#!/usr/bin/env python3
"""https://leetcode.com/problems/sort-characters-by-frequency/"""

from collections import Counter

from tools.lc_tools import benchmark, pretty_eval


class SolutionInit:
    # Time / Space: O(n log n) / O(n)
    def frequencySort(self, s: str) -> str:
        freqs = Counter(s)
        s_list = list(s)
        s_list.sort()
        s_list.sort(key=freqs.get, reverse=True)
        s_sorted = ''.join(s_list)
        return s_sorted


class SolutionAlt:
    # Time / Space: O(n log k) / O(n)
    def frequencySort(self, s: str) -> str:
        c_freqs = Counter(s)
        builder = [c * freq for c, freq in c_freqs.most_common()]
        s_sorted = ''.join(builder)
        return s_sorted


class SolutionPref:
    # Time / Space: O(n) / O(n)
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


if __name__ == '__main__':
    # Setup
    s_init = SolutionInit()
    s_alt = SolutionAlt()
    s_pref = SolutionPref()
    solutions = [s_init, s_alt, s_pref]
    method = 'frequencySort'

    # Examples
    inputs = ['tree', 'cccaaa', 'Aabb']
    outputs = ['eert', 'aaaccc', 'bbAa']
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 100
    args = 'abcdefghijklmnopqrstuvwxyz' * 1000
    benchmark(solutions, method, args, number)
