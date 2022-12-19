#!/usr/bin/env python3
"""https://leetcode.com/problems/maximum-frequency-stack/"""

from collections import defaultdict
from heapq import heappop, heappush


class SolutionInit:
    # Time / Space: O(n log k) / O(n)
    def __init__(self):
        self.pq = []
        self.clock = 0
        self.num_freqs = defaultdict(int)

    def push(self, val: int) -> None:
        pq, num_freqs, clock = self.pq, self.num_freqs, self.clock
        num_freqs[val] += 1
        freq = num_freqs[val]
        heappush(pq, (-freq, clock, val))
        self.clock -= 1

    def pop(self) -> int:
        freq, clock, val = heappop(self.pq)
        self.num_freqs[val] -= 1
        return val


class SolutionPref:
    # Time / Space: O(1) / O(n)
    def __init__(self):
        self.num_freqs = defaultdict(int)
        self.freq_stacks = defaultdict(list)
        self.freq_max = 0

    def push(self, val: int) -> None:
        freq = self.num_freqs[val] = self.num_freqs[val] + 1
        self.freq_stacks[freq].append(val)
        self.freq_max = max(self.freq_max, freq)

    def pop(self) -> int:
        freq_stack = self.freq_stacks[self.freq_max]
        val = freq_stack.pop()
        self.num_freqs[val] -= 1
        if not freq_stack:
            self.freq_max -= 1
        return val


if __name__ == '__main__':
    fs_init = SolutionInit()
    fs_pref = SolutionPref()
    nums = [5, 7, 5, 7, 4, 5]
    for num in nums:
        fs_init.push(num)
        fs_pref.push(num)

    print(fs_init.pop(), fs_pref.pop())
    print(fs_init.pop(), fs_pref.pop())
    print(fs_init.pop(), fs_pref.pop())
    print(fs_init.pop(), fs_pref.pop())
    print(fs_init.pop(), fs_pref.pop())
    print(fs_init.pop(), fs_pref.pop())
