#!/usr/bin/env python3
"""https://leetcode.com/problems/k-closest-points-to-origin/"""

from heapq import heappop, heappush
import math
from random import randint


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2)

        def partition(l: int, r: int, i_pivot: int) -> int:
            pivot = dist(points[i_pivot])
            points[i_pivot], points[r] = points[r], points[i_pivot]

            i_swap = l
            for i in range(l, r):
                if dist(points[i]) < pivot:
                    points[i], points[i_swap] = points[i_swap], points[i]
                    i_swap += 1

            points[r], points[i_swap] = points[i_swap], points[r]
            return i_swap

        def quickselect(l: int, r: int, k: int) -> None:
            if l >= r: return

            i_pivot = randint(l, r)
            i_pivot = partition(l, r, i_pivot)

            if k == i_pivot:
                return
            elif k < i_pivot:
                quickselect(l, i_pivot - 1, k)
            else:
                quickselect(i_pivot + 1, r, k)

        quickselect(0, len(points) - 1, k)
        return points[:k]


class SolutionAlt:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2)
        distpoints = []

        for p in points:
            heappush(distpoints, (-dist(p), p))
            if len(distpoints) > k:
                heappop(distpoints)

        k_closest = [dp[1] for dp in distpoints]
        return k_closest
