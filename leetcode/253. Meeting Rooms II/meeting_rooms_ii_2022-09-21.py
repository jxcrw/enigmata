#!/usr/bin/env python3
"""https://leetcode.com/problems/meeting-rooms-ii/"""

from heapq import heappop, heappush


class Solution:
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
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        rooms = 0
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        e = 0
        for s in range(len(intervals)):
            if starts[s] >= ends[e]:
                rooms -= 1
                e += 1
            rooms += 1
        return rooms
