#!/usr/bin/env python3
"""https://leetcode.com/problems/maximum-frequency-stack/"""

from collections import defaultdict


class Solution:
    def __init__(self):
        self.num_freqs = defaultdict(int)
        self.freq_stacks = defaultdict(list)
        self.freq_max = 0

    def push(self, val: int) -> None:
        freq = self.num_freqs[val] = self.num_freqs[val] + 1
        self.freq_max = max(self.freq_max, freq)
        self.freq_stacks[freq].append(val)

    def pop(self) -> int:
        freq_stack = self.freq_stacks[self.freq_max]
        val = freq_stack.pop()
        self.num_freqs[val] -= 1
        if not freq_stack: self.freq_max -= 1
        return val
