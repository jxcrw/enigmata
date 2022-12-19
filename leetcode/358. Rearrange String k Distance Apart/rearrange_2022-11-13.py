#!/usr/bin/env python3
"""https://leetcode.com/problems/rearrange-string-k-distance-apart/"""

from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1: return s

        c_freqs = Counter(s)
        pq = [(-freq, c) for c, freq in c_freqs.items()]
        heapify(pq)

        builder, cooler = [], {}
        while pq:
            freq, c = heappop(pq)
            builder.append(c)

            freq += 1
            if freq < 0:
                cooler[c] = [freq, c]

            if len(builder) >= k and builder[-k] in cooler:
                freq_cool, c_cool = cooler.pop(builder[-k])
                heappush(pq, (freq_cool, c_cool))

        solution_found = len(builder) == len(s)
        return ''.join(builder) if solution_found else ''
