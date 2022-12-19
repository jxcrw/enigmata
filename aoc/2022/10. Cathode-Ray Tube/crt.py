#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/10"""

from collections import deque
from typing import Any

from tools.aoc import load, prettyprint, superparse

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=0)
P, _ = load('_puzzle.txt', pre=0)

seps = deque([r'\n', r' '])
args = {'seps': seps, 'str_to_num': True, 'extract_num': False}
X = superparse(X, **args)
P = superparse(P, **args)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def sum_signal_strengths(program: list[list[Any]]) -> int:
    """Compute sum of interesting signal strengths."""
    clock, X = 0, 1
    strengths = []
    strength = lambda: clock * X

    for line in program:
        clock += 1
        command = line[0]
        strengths.append(strength())

        if command == 'addx':
            clock += 1
            amount = line[1]
            strengths.append(strength())
            X += amount

    interesting = strengths[19::40]
    sum_interesting = sum(interesting)
    return sum_interesting


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
def render_image(program: list[list[Any]]) -> str:
    """Render image on CRT screen based on sprite position."""
    clock, X = 0, 1
    screen, col = '', 0

    def draw():
        nonlocal screen, col
        sprite = [X - 1, X, X + 1]
        pixel = '█' if col in sprite else ' '
        screen += pixel
        col += 1
        if col == 40:
            screen += '\n'
            col = 0

    for line in program:
        clock += 1
        command = line[0]
        draw()

        if command == 'addx':
            clock += 1
            amount = line[1]
            draw()
            X += amount

    return screen


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = sum_signal_strengths(X)
P1 = sum_signal_strengths(P)
prettyprint(X1, P1)

X2 = render_image(X)
P2 = render_image(P)
prettyprint(X2, P2)
