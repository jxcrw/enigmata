#!/usr/bin/env python3
"""https://leetcode.com/problems/interval-list-intersections/"""

import timeit


class Solution:
    # Time / Space: O(|A|+|B|) / O(|A|+|B|)
    def intervalIntersection(self, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        intervals = []
        i = j = 0
        while i < len(A) and j < len(B):
            A_start, A_end = A[i]
            B_start, B_end = B[j]

            lo = max(A_start, B_start)
            hi = min(A_end, B_end)
            if lo <= hi: intervals.append([lo, hi])

            if A_end < B_end: i += 1
            else: j += 1
        return intervals


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]])
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(solution.intervalIntersection(A, B))

    # Example 2 (Expected Output: [])
    A, B = [[1, 3], [5, 9]], []
    print(solution.intervalIntersection(A, B))

    # Benchmarking
    number = 10_000
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(timeit.timeit(lambda: solution.intervalIntersection(A, B), number=number))
