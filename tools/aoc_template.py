#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/n"""

from bisect import bisect_right, bisect_left
from collections import Counter, deque
import operator
from functools import reduce
import re

from tools.aoc import * # type: ignore

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, pre_X = load('_example.txt', pre=0)
P, pre_P = load('_puzzle.txt', pre=0)

p_seps = deque([r''])
p_args = {'seps': p_seps, 'str_to_num': 'int', 'extract_num': False}
pre_X = superparse(pre_X, **p_args)
pre_P = superparse(pre_P, **p_args)

seps = deque([r'\n'])
args = {'seps': seps, 'str_to_num': 'int', 'extract_num': False}
X = superparse(X, **args)
P = superparse(P, **args)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def part1(data):
    pass


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
def part2(data):
    pass


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = part1(X)
P1 = part1(P)
prettyprint(X1, P1)

X2 = part2(X)
P2 = part2(P)
prettyprint(X2, P2)
