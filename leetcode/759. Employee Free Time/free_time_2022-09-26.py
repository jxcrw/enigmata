#!/usr/bin/env python3
"""https://leetcode.com/problems/employee-free-time/"""

import heapq
import itertools


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        free_times = []
        intervals = sorted(itertools.chain(*schedule), key=lambda x: x.start)
        last_end = intervals[0].end

        for i in intervals[1:]:
            if i.start > last_end:
                free_times.append(Interval(last_end, i.start))
            last_end = max(last_end, i.end)

        return free_times


class SolutionAlternate:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        free_times = []
        intervals = heapq.merge(*schedule, key=lambda x: x.start)
        last_end = next(intervals).end

        for i in intervals:
            if i.start > last_end:
                free_times.append(Interval(last_end, i.start))
            last_end = max(last_end, i.end)

        return free_times


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
