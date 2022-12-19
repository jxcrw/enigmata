#!/usr/bin/env python3
"""https://leetcode.com/problems/employee-free-time/"""

import heapq
from itertools import chain
import timeit


class SolutionInitial:
    # Time / Space: O(n log n) / O(n) where n is total number of intervals
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted(chain(*schedule), key=lambda x: x.start)
        free_times, end = [], intervals[0].end
        for i in intervals[1:]:
            if i.start > end:
                free_times.append(Interval(end, i.start))
            end = max(end, i.end)
        return free_times


class SolutionPreferred:
    # Time / Space: O(n log k) / O(k), where n is total number of intervals and k is number of employees
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

    def __repr__(self):
        return f'[{self.start}, {self.end}]'


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [[3, 4]])
    schedule = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]
    print(s_init.employeeFreeTime(schedule))
    print(s_pref.employeeFreeTime(schedule))

    # Example 2 (Expected Output: [[5, 6], [7, 9]])
    schedule = [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]]
    print(s_init.employeeFreeTime(schedule))
    print(s_pref.employeeFreeTime(schedule))

    # Benchmarking
    number = 10_000
    schedule = [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]]
    print(timeit.timeit(lambda: s_init.employeeFreeTime(schedule), number=number))
    print(timeit.timeit(lambda: s_pref.employeeFreeTime(schedule), number=number))
