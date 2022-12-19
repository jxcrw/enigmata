#!/usr/bin/env python3
"""https://leetcode.com/problems/reorganize-string/"""

from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        c_freqs = Counter(s)
        pq = [(-freq, c) for c, freq in c_freqs.items()]
        heapify(pq)

        builder = []
        freq_prev, c_prev = 0, ''
        while pq:
            freq, c = heappop(pq)
            builder.append(c)

            if freq_prev < 0:
                heappush(pq, (freq_prev, c_prev))

            freq += 1
            freq_prev, c_prev = freq, c

        solution_found = len(builder) == len(s)
        return ''.join(builder) if solution_found else ''
