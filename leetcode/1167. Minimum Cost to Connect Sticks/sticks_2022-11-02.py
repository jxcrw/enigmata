#!/usr/bin/env python3
"""https://leetcode.com/problems/minimum-cost-to-connect-sticks/"""

from heapq import heapify, heappop, heappushpop


class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        min_cost = 0
        heapify(sticks)
        while len(sticks) > 1:
            cost = heappop(sticks) + sticks[0]
            min_cost += cost
            heappushpop(sticks, cost)
        return min_cost
