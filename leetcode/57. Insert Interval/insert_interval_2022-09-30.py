#!/usr/bin/env python3
"""https://leetcode.com/problems/insert-interval/"""

class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        START, END = 0, 1
        left, right = [], []
        start, end = new_interval[START], new_interval[END]

        for i in intervals:
            if i[END] < start:
                left.append(i)
            elif i[START] > end:
                right.append(i)
            else:
                start = min(start, i[START])
                end = max(end, i[END])

        return left + [[start, end]] + right
