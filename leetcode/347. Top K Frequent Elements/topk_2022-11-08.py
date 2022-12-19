#!/usr/bin/env python3
"""https://leetcode.com/problems/top-k-frequent-elements/"""

from collections import Counter
from heapq import heappop, heappush, nlargest
from random import randint


class Solution:
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
            if l == r: return

            p = randint(l, r)
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


class SolutionAlt:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_freqs = Counter(nums)
        h = []
        for num, freq in num_freqs.items():
            heappush(h, (freq, num))
            if len(h) > k:
                heappop(h)
        top_k = [nf[1] for nf in h]
        return top_k

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqs = Counter(nums)
        top_k = nlargest(k, freqs.keys(), key=freqs.get)
        return top_k
