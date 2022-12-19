#!/usr/bin/env python3
"""https://leetcode.com/problems/task-scheduler/"""

from collections import Counter
from heapq import heapify, heappop, heappush
import itertools

from tools.lc_tools import benchmark, init_solutions, pretty_eval


class SolutionInit:
    # Time / Space: ? / O(n)
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if n == 0: return len(tasks)

        task_freqs = Counter(tasks)
        pq = [(-freq, task) for task, freq in task_freqs.items()]
        heapify(pq)

        schedule, cooler, time = [], [], 0
        while pq or cooler:
            if time % (n + 1) == 0:
                for freq, task in cooler:
                    heappush(pq, (freq, task))
                cooler.clear()

            if pq:
                freq, task = heappop(pq)
                schedule.append(task)
                freq += 1
                if freq < 0:
                    cooler.append((freq, task))
            else:
                schedule.append('idle')

            time += 1

        runtime = len(schedule)
        return runtime


class SolutionPref:
    # Time / Space: O(n) / O(1)
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freqs = list(Counter(tasks).values())
        freq_max = max(freqs)
        last_row = freqs.count(freq_max)
        total = (freq_max - 1) * (n + 1) + last_row

        runtime = max(total, len(tasks))
        return runtime


if __name__ == '__main__':
    # Setup
    solutions = init_solutions(globals())
    method = 'leastInterval'

    # Examples
    inputs = [(['A', 'A', 'A', 'B', 'B', 'B'], 2), (['A', 'A', 'A', 'B', 'B', 'B'], 0), (['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2)]
    outputs = [8, 6, 16]
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 250
    args = (list('abcdefghijklmnopqrstuvwxyz' * 200), 2)
    benchmark(solutions, method, args, number)
