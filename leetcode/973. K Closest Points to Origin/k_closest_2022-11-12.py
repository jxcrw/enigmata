#!/usr/bin/env python3
"""https://leetcode.com/problems/k-closest-points-to-origin/"""

import math
from heapq import heappop, heappush
from random import randint


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2)

        def partition(l: int, r: int, p: int) -> int:
            pivot = dist(points[p])
            points[p], points[r] = points[r], points[p]

            i_swap = l
            for i in range(l, r):
                if dist(points[i]) < pivot:
                    points[i], points[i_swap] = points[i_swap], points[i]
                    i_swap += 1

            points[r], points[i_swap] = points[i_swap], points[r]
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

        n = len(points)
        quickselect(0, n - 1, k)
        k_closest = points[:k]
        return k_closest


class SolutionAlt:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2)
        dist_points = []

        for p in points:
            heappush(dist_points, (-dist(p), p))
            if len(dist_points) > k:
                heappop(dist_points)

        k_closest = [dp[1] for dp in dist_points]
        return k_closest
