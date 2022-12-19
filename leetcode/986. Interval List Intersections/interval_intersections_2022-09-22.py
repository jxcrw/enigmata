#!/usr/bin/env python3
"""https://leetcode.com/problems/interval-list-intersections/"""

class Solution:
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
