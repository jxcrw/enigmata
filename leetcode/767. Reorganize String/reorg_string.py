#!/usr/bin/env python3
"""https://leetcode.com/problems/reorganize-string/"""

from collections import Counter
from heapq import heapify, heappop, heappush

from tools.lc_tools import benchmark, init_solutions, pretty_eval


class SolutionInit:
    # Time / Space: O(n log k) / O(n); n = total chars, k = unique chars
    def reorganizeString(self, s: str) -> str:
        c_freqs = Counter(s)
        pq = [(-freq, c) for c, freq in c_freqs.items()]
        heapify(pq)

        builder = []
        prev_freq, prev_c = 0, ''
        while pq:
            freq, c = heappop(pq)
            builder.append(c)

            if prev_freq < 0:
                heappush(pq, (prev_freq, prev_c))

            freq += 1
            prev_freq, prev_c = freq, c

        solution_found = len(builder) == len(s)
        return ''.join(builder) if solution_found else ''


if __name__ == '__main__':
    # Setup
    solutions = init_solutions(globals())
    method = 'reorganizeString'

    # Examples
    inputs = ['aaab', 'aab', 'abbcccdddd']
    outputs = ['', 'aba', 'dcdbcdabcd']
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 250
    args = 'abcdefghijklmnopqrstuvwxyz' * 250
    benchmark(solutions, method, args, number)
