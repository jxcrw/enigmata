#!/usr/bin/env python3
"""https://adventofcode.com/2021/day/1"""

from tools.aoc import *

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
ex = '''
199
200
208
210
200
207
240
269
260
263
'''
data = load('input.txt')

ex = preprocess(ex)
data = preprocess(data)
print(f'ex: {len(ex)} | data: {len(data)}')

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def part1(nums):
    r = 0
    for i in range(len(nums)):
        if i == 0: continue
        if nums[i] > nums[i - 1]:
            r += 1
    return r

# --- Results ---
x1, s1 = part1(ex), part1(data)
prettyprint(x1, s1)
# submit('part1', s1)

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
def part2(nums):
    r, sum_prev = 0, float('inf')

    for i in range(len(nums)):
        if i in [0, 1]: continue

        sum_win = nums[i] + nums[i - 1] + nums[i - 2]
        if sum_win > sum_prev:
            r += 1

        sum_prev = sum_win

    return r

# --- Results ---
x2, s2 = part2(ex), part2(data)
prettyprint(x2, s2)
# submit('part2', s2)
