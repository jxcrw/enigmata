#!/usr/bin/env python3
"""https://leetcode.com/problems/task-scheduler/"""

from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freqs = list(Counter(tasks).values())
        freq_max = max(freqs)
        last_row = freqs.count(freq_max)
        total = (freq_max - 1) * (n + 1) + last_row

        runtime = max(total, len(tasks))
        return runtime
