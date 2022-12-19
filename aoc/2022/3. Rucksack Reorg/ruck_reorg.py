#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/3"""

from collections import deque

from tools.aoc import load, prettyprint, superparse
from tools.dsa.common import chunk

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=0)
P, _ = load('_puzzle.txt', pre=0)

seps = deque(['\n'])
args = {'seps': seps, 'str_to_num': '', 'extract_num': False}
X = superparse(X, **args)
P = superparse(P, **args)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
PRIORITIES = {c: i + 1 for i, c in enumerate(CHARS)}


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def sum_item_priorities(data):
    """Compute sum of priorities of common items in rucksack compartments."""
    total_priority = 0

    for ruck in data:
        mid = len(ruck) // 2
        item1, item2 = ruck[:mid], ruck[mid:]

        common, = set(item1) & set(item2)
        priority = PRIORITIES[common]

        total_priority += priority

    return total_priority


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
def sum_badge_priorities(data):
    """Compute sum of priorities of rucksack badges."""
    total_priority = 0
    groups = chunk(data, 3)

    for group in groups:
        rucks = [set(ruck) for ruck in group]
        badge, = set.intersection(*rucks)

        priority = PRIORITIES[badge]
        total_priority += priority

    return total_priority


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = sum_item_priorities(X)
P1 = sum_item_priorities(P)
prettyprint(X1, P1)

X2 = sum_badge_priorities(X)
P2 = sum_badge_priorities(P)
prettyprint(X2, P2)
