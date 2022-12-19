#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/4"""

from collections import deque

from tools.aoc import load, prettyprint, superparse

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=0)
P, _ = load('_puzzle.txt', pre=0)

seps = deque(['\n', ',', '-'])
args = {'seps': seps, 'str_to_num': 'int', 'extract_num': False}
X = superparse(X, **args)
P = superparse(P, **args)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def count_fullcontains(pairs: list[list[int]]) -> int:
    """Count number of interval pairs in which one fully contains the other."""
    count = 0
    for pair in pairs:
        pair.sort(key=lambda x: (x[0], -x[1])) # Sort by start ***and then within that, by end***
        a, b = pair

        if a[0] <= b[0] and b[1] <= a[1]: # Like how this looks exactly like what it does :)
            count += 1

    return count


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
def count_overlaps(pairs: list[list[int]]) -> int:
    """Count number of intervals pairs that overlap."""
    count = 0

    for pair in pairs:
        pair.sort(key=lambda x: x[0])
        a, b = pair

        if a[1] >= b[0]:
            count += 1

    return count


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = count_fullcontains(X)
P1 = count_fullcontains(P)
prettyprint(X1, P1)

X2 = count_overlaps(X)
P2 = count_overlaps(P)
prettyprint(X2, P2)
