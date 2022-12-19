#!/usr/bin/env python3
"""Sliding window stuff"""

from collections import Counter


class Slindow:
    """A sliding window. Backed by a Counter."""
    def __init__(self, data: str, start: int = 0, end: int = 0):
        self.data = data
        self.start = start
        self.end = end
        self.frame = data[start:end]
        self.window = Counter(data[start:end])

    def slide(self):
        """Slide window and update internal state accordingly."""
        data, window = self.data, self.window
        dS, dE = data[self.start], data[self.end]

        window[dS] -= 1
        window[dE] += 1
        if window[dS] == 0: window.pop(dS)

        self.start += 1
        self.end += 1
        self.frame = data[self.start:self.end]
