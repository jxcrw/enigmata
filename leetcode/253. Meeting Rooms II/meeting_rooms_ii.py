#!/usr/bin/env python3
"""https://leetcode.com/problems/meeting-rooms-ii/"""

from heapq import heappop, heappush
from random import randint
import timeit


class SolutionPreferred:
    # Time / Space: O(n log n) / O(n)
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        end_times = []
        intervals.sort(key=lambda x: x[0])
        heappush(end_times, intervals[0][1])

        for i in intervals[1:]:
            if i[0] >= end_times[0]:
                heappop(end_times)
            heappush(end_times, i[1])
        return len(end_times)


class SolutionAlternate:
    # Time / Space: O(n log n) / O(n)
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        rooms = 0
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        e = 0
        for start in starts:
            if start >= ends[e]:
                rooms -= 1
                e += 1
            rooms += 1
        return rooms


if __name__ == '__main__':
    s_pref = SolutionPreferred()
    s_alt = SolutionAlternate()

    # Example 1 (Expected Output: 2)
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(s_pref.minMeetingRooms(intervals))
    print(s_alt.minMeetingRooms(intervals))

    # Example 2 (Expected Output: 1)
    intervals = [[7, 10], [2, 4]]
    print(s_pref.minMeetingRooms(intervals))
    print(s_alt.minMeetingRooms(intervals))

    # Example 3 (Expected Output: 2)
    intervals = [[9, 10], [4, 9], [4, 17]]
    print(s_pref.minMeetingRooms(intervals))
    print(s_alt.minMeetingRooms(intervals))

    # Example 4 (Expected Output: 4)
    intervals = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
    print(s_pref.minMeetingRooms(intervals))
    print(s_alt.minMeetingRooms(intervals))

    # Benchmarking
    number = 100
    intervals1 = [[randint(0, 1_000_000), randint(0, 1_000_000)] for _ in range(10_000)]
    intervals2 = intervals1[:]
    print(timeit.timeit(lambda: s_pref.minMeetingRooms(intervals1), number=number))
    print(timeit.timeit(lambda: s_alt.minMeetingRooms(intervals2), number=number))
