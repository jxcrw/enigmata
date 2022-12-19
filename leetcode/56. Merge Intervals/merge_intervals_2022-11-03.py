#!/usr/bin/env python3
"""https://leetcode.com/problems/merge-intervals/"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            if not merged or i[0] > merged[-1][1]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged
