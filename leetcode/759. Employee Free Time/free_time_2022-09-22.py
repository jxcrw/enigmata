#!/usr/bin/env python3
"""https://leetcode.com/problems/employee-free-time/"""

import heapq
from itertools import chain


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted(chain(*schedule), key=lambda x: x.start)
        free_times, end = [], intervals[0].end
        for i in intervals[1:]:
            if i.start > end:
                free_times.append(Interval(end, i.start))
            end = max(end, i.end)
        return free_times


class SolutionAlternate:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = heapq.merge(*schedule, key=lambda x: x.start)
        free_times, end = [], next(intervals).end
        for i in intervals:
            if i.start > end:
                free_times.append(Interval(end, i.start))
            end = max(end, i.end)
        return free_times


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
