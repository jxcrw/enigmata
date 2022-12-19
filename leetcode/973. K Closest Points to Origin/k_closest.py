#!/usr/bin/env python3
"""https://leetcode.com/problems/k-closest-points-to-origin/"""

import heapq
from heapq import heappop, heappush
from math import sqrt
import random

from tools.lc_tools import benchmark, pretty_eval


class SolutionTimsort:
    # Time / Space: O(n log n) / O(n)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = lambda p: sqrt(p[0] ** 2 + p[1] ** 2)
        points.sort(key=dist)
        return points[:k]


class PointDistance:
    def __init__(self, point: list[int]):
        self.point = point
        self.distance = sqrt(point[0] ** 2 + point[1] ** 2)


class SolutionQuickSelectLame:
    # Time / Space: O(n) / O(n)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        point_distances = [PointDistance(p) for p in points]
        kth_closest = self._quickselect(point_distances, k)

        k_closest = [pd.point for pd in point_distances if pd.distance <= kth_closest.distance]
        return k_closest

    def _quickselect(self, point_distances: list[PointDistance], k: int) -> PointDistance:
        if not point_distances: return PointDistance([0, 0])

        pivot = random.choice(point_distances)
        left = [pd for pd in point_distances if pd.distance < pivot.distance]
        mid = [pd for pd in point_distances if pd.distance == pivot.distance]
        right = [pd for pd in point_distances if pd.distance > pivot.distance]
        L, M = len(left), len(mid)

        if k <= L:
            return self._quickselect(left, k)
        elif k <= L + M:
            return pivot
        else:
            return self._quickselect(right, k - M - L)


class SolutionHeapQSimple:
    # Time / Space: O(n log k) / O(1)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = lambda p: sqrt(p[0] ** 2 + p[1] ** 2)
        k_closest = heapq.nsmallest(k, points, key=dist)
        return k_closest


class SolutionHeapQFull:
    # Time / Space: O(n log k) / O(1)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = lambda p: sqrt(p[0] ** 2 + p[1] ** 2)

        distpoints = []
        for point in points:
            heappush(distpoints, (-dist(point), point))
            if len(distpoints) > k:
                heappop(distpoints)
        return [dp[1] for dp in distpoints]


class SolutionQuickselect:
    # Time / Space: O(n) / O(1)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = lambda p: sqrt(p[0] ** 2 + p[1] ** 2)

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

            i_pivot = random.randint(l, r)
            i_pivot = partition(l, r, i_pivot)

            if k == i_pivot:
                return
            elif k < i_pivot:
                quickselect(l, i_pivot - 1, k)
            else:
                quickselect(i_pivot + 1, r, k)

        quickselect(0, len(points) - 1, k)
        return points[:k]


if __name__ == '__main__':
    # Setup
    s_timsort = SolutionTimsort()
    s_quickselect_lame = SolutionQuickSelectLame()
    s_heapq_simple = SolutionHeapQSimple()
    s_heapq_full = SolutionHeapQFull()
    s_quickselect = SolutionQuickselect()
    solutions = [s_timsort, s_quickselect_lame, s_heapq_simple, s_heapq_full, s_quickselect]
    method = 'kClosest'

    # Examples
    inputs = [([[1, 3], [-2, 2]], 1), ([[3, 3], [5, -1], [-2, 4]], 2)]
    outputs = [[[-2, 2]], [[3, 3], [-2, 4]]]
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 10_000

    # Benchmarking
    number = 100
    points = [[x, x] for x in range(10_000)]
    random.shuffle(points)
    k = 5000
    args = (points, k)
    benchmark(solutions, method, args, number)
