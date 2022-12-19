#!/usr/bin/env python3
"""https://leetcode.com/problems/minimum-cost-to-connect-sticks/"""

from heapq import heapify, heappop, heappush, heappushpop
import random

from tools.lc_tools import benchmark, pretty_eval


class SolutionInit:
    # Time / Space: O(n log n) / O(n)
    def connectSticks(self, sticks: list[int]) -> int:
        min_cost, h = 0, sticks[:]
        heapify(h)

        while len(h) > 1:
            s1, s2 = heappop(h), heappop(h)
            cost = s1 + s2

            min_cost += cost
            heappush(h, cost)

        return min_cost


class SolutionPref:
    # Time / Space: O(n log n) / O(n)
    def connectSticks(self, sticks: list[int]) -> int:
        min_cost, h = 0, sticks[:]
        heapify(h)

        while len(h) > 1:
            cost = heappop(h) + h[0]
            min_cost += cost
            heappushpop(h, cost)

        return min_cost


if __name__ == '__main__':
    # Setup
    s_init = SolutionInit()
    s_pref = SolutionPref()
    solutions = [s_init, s_pref]
    method = 'connectSticks'

    # Examples
    inputs = [[2, 4, 3], [1, 8, 3, 5], [5]]
    outputs = [14, 30, 0]
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 100
    args = list(range(10_000))
    random.shuffle(args)
    benchmark(solutions, method, args, number)

