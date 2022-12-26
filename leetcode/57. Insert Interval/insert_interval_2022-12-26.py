#!/usr/bin/env python3
"""https://leetcode.com/problems/insert-interval/"""

class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        START, END = 0, 1
        start, end = new_interval
        lefts, rights = [], []

        for i in intervals:
            if i[END] < start:
                lefts.append(i)
            elif i[START] > end:
                rights.append(i)
            else:
                start = min(start, i[START])
                end = max(end, i[END])

        inserted = lefts + [[start, end]] + rights
        return inserted
