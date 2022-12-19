#!/usr/bin/env python3
"""https://leetcode.com/problems/insert-interval/"""

import timeit


class SolutionInitial:
    # Time / Space: O(n) * 3 / O(n)
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        if not intervals:
            intervals.append(new_interval)
            return intervals

        for i, interval in enumerate(intervals):
            if new_interval[0] < interval[0]:
                intervals.insert(i, new_interval)
                break
            elif i == len(intervals) - 1:
                intervals.append(new_interval)
                break

        intervals = self._merge(intervals)
        return intervals

    def _merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


class SolutionPreferred:
    # Time / Space: O(n) / O(n)
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


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [[1, 5], [6, 9]])
    intervals, new_interval = [[1, 3], [6, 9]], [2, 5]
    print(s_init.insert(intervals, new_interval))
    print(s_pref.insert(intervals, new_interval))

    # Example 2 (Expected Output: [[1, 2], [3, 10], [12, 16]])
    intervals, new_interval = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    print(s_init.insert(intervals, new_interval))
    print(s_pref.insert(intervals, new_interval))

    # Example 3 (Expected Output: [[1, 7]])
    intervals, new_interval = [[1, 5]], [2, 7]
    print(s_init.insert(intervals, new_interval))
    print(s_pref.insert(intervals, new_interval))

    # Benchmarking
    number = 1_000
    intervals, new_interval = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    print(timeit.timeit(lambda: s_init.insert(intervals, new_interval), number=number))
    print(timeit.timeit(lambda: s_pref.insert(intervals, new_interval), number=number))
