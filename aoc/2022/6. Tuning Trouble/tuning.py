#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/6"""

from collections import Counter

from tools.aoc import load, prettyprint

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=0)
P, _ = load('_puzzle.txt', pre=0)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ New Features
# └─────────────────────────────────────────────────────────────────────────────
class Slindow:
    """A sliding window backed by a Counter."""
    def __init__(self, data: str, start: int= 0 , end: int = 0):
        self.start = start
        self.end = end
        self.data = data
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


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1/2
# └─────────────────────────────────────────────────────────────────────────────
N_SOP = 4   # Length of start-of-packet marker
N_SOM = 14  # Length of start-of-message marker

def find_eom(data: str, target_len: int) -> int:
    """Find end of some marker of specified length within a datastream."""
    slindow = Slindow(data, start=0, end=target_len)
    marker = slindow.window

    while len(marker) < target_len:
        slindow.slide()

    end = slindow.end
    return end


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = find_eom(X, N_SOP)
P1 = find_eom(P, N_SOP)
prettyprint(X1, P1)

X2 = find_eom(X, N_SOM)
P2 = find_eom(P, N_SOM)
prettyprint(X2, P2)
