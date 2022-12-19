#!/usr/bin/env python3
"""https://leetcode.com/problems/top-k-frequent-elements/"""

from collections import Counter
from heapq import heappop, heappush, nlargest
import random

from tools.lc_tools import benchmark, pretty_eval


class SolutionInit:
    # Time / Space: O(n log n) / O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_freqs = Counter(nums)
        nums_sorted = [k for k, v in sorted(num_freqs.items(), key=lambda i: i[1], reverse=True)]
        return nums_sorted[:k]


class SolutionAlt:
    # Time / Space: O(n log k) / O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_freqs = Counter(nums)
        h = []
        for num, freq in num_freqs.items():
            heappush(h, (freq, num))
            if len(h) > k:
                heappop(h)
        top_k = [nf[1] for nf in h]
        return top_k


class SolutionAlt2:
    # Time / Space: O(n log k) / O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_freqs = Counter(nums)
        top_k = nlargest(k, num_freqs.keys(), key=num_freqs.get)
        return top_k


class SolutionPref:
    # Time / Space: O(n) / O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqs = Counter(nums)
        unique = list(freqs.keys())

        def partition(l: int, r: int, p: int) -> int:
            pivot = freqs[unique[p]]
            unique[p], unique[r] = unique[r], unique[p]

            i_swap = l
            for i in range(l, r):
                if freqs[unique[i]] < pivot:
                    unique[i], unique[i_swap] = unique[i_swap], unique[i]
                    i_swap += 1

            unique[r], unique[i_swap] = unique[i_swap], unique[r]
            return i_swap

        def quickselect(l: int, r: int, k: int) -> None:
            if l >= r: return

            p = random.randint(l, r)
            p = partition(l, r, p)

            if k == p:
                return
            elif k < p:
                quickselect(l, p - 1, k)
            else:
                quickselect(p + 1, r, k)

        n = len(unique)
        quickselect(0, n - 1, n - k)
        return unique[n - k:]


if __name__ == '__main__':
    # Setup
    s_init = SolutionInit()
    s_alt = SolutionAlt()
    s_alt2 = SolutionAlt2()
    s_pref = SolutionPref()
    solutions = [s_init, s_alt, s_alt2, s_pref]
    method = 'topKFrequent'

    # Examples
    inputs = [([1, 1, 1, 2, 2, 3], 2), ([1], 1), ([5, 3, 1, 1, 1, 3, 73, 1], 2)]
    outputs = [[1, 2], [1], [1, 3]]
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 100
    nums = list(range(1000)) * 10
    random.shuffle(nums)
    args = (nums, 500)
    benchmark(solutions, method, args, number)
