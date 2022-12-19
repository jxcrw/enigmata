#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/1"""

from collections import deque
import heapq

from tools.aoc import load, prettyprint, superparse

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=0)
P, _ = load('_puzzle.txt', pre=0)

seps = deque([r'\n\n', r'\n'])
args = {'seps': seps, 'str_to_num': 'int', 'extract_num': False}
X = superparse(X, **args)
P = superparse(P, **args)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def sum_max_cals(inventories: list[list[int]]) -> int:
    """Compute sum of calories in largest food inventory."""
    max_cals = 0
    for inventory in inventories:
        total = sum(int(i) for i in inventory)
        max_cals = max(max_cals, total)
    return max_cals


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
def sum_top3_max_cals(inventories: list[list[int]]) -> int:
    """Compute sum of calories in 3 largest food inventories."""
    totals = []
    for inventory in inventories:
        total = sum(int(i) for i in inventory)
        totals.append(total)

    top3 = heapq.nlargest(3, totals)
    sum_top3 = sum(top3)
    return sum_top3


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = sum_max_cals(X)
P1 = sum_max_cals(P)
prettyprint(X1, P1)

X2 = sum_top3_max_cals(X)
P2 = sum_top3_max_cals(P)
prettyprint(X2, P2)
