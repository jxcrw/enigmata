#!/usr/bin/env python3
"""https://leetcode.com/problems/merge-intervals/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n log n) / O(n)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        combined = []
        for interval in intervals:
            recentest = combined[-1]
            recentest_start, recentest_end = recentest[0], recentest[1]
            current_start, current_end = intervals[i][0], intervals[i][1]
            if current_start <= recentest_end:
                end = max(recentest_end, current_end)
                combined[-1] = [recentest_start, end]
            else:
                combined.append(intervals[i])
        return combined

class SolutionPreferred:
    # Time / Space: O(n log n) / O(n)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [[1, 6], [8, 10], [15, 18]])
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(s_init.merge(intervals))
    print(s_pref.merge(intervals))

    # Example 2 (Expected Output: [[1, 5]])
    intervals = [[1, 4], [4, 5]]
    print(s_init.merge(intervals))
    print(s_pref.merge(intervals))

    # Example 3 (Expected Output: [[0, 4]])
    intervals = [[1, 4], [0, 4]]
    print(s_init.merge(intervals))
    print(s_pref.merge(intervals))

    # Benchmarking
    number = 100_000
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(timeit.timeit(lambda: s_init.merge(intervals), number=number))
    print(timeit.timeit(lambda: s_pref.merge(intervals), number=number))
