#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/9"""

from collections import deque
from math import sqrt
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
# │ New Features
# └─────────────────────────────────────────────────────────────────────────────
class Point:
    """A point in 2D space."""

    PLANCK = sqrt(2)

    def __init__(self, x: int = 0, y: int = 0, name: str = ''):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        return f'<{self.x}, {self.y}, {self.name}>'

    def pos(self) -> tuple[int, int]:
        """Get position of point."""
        return self.x, self.y

    def move(self, direction: str, amount: int = 0) -> None:
        """Move point in direction by given amount."""
        match direction:
            case 'L': self.x -= amount
            case 'R': self.x += amount
            case 'U': self.y += amount
            case 'D': self.y -= amount
            case _:
                raise Exception('Unsupported direction.')

    def follow(self, leader: 'Point') -> None:
        """Maintain contact with another point."""
        dist = self.distance(leader)
        if dist > self.PLANCK:
            hop_x = round((leader.x - self.x) / self.PLANCK) # Magic, any divisor ≥ ≈1.4 and < 2 works ¯\_(ツ)_/¯
            hop_y = round((leader.y - self.y) / self.PLANCK)
            self.x += hop_x
            self.y += hop_y

    def distance(self, point: 'Point') -> float:
        """Compute the distance from this point to another point."""
        x1, x2 = self.x, point.x
        y1, y2 = self.y, point.y
        dist = sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return dist


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1/2
# └─────────────────────────────────────────────────────────────────────────────
def count_tail_positions(motions: list[list[Any]], knots: int) -> int:
    """Count positions visited by the tail of a knotted rope just going through the motions."""
    rope = [Point(0, 0, str(k)) for k in range(knots)]
    true_head = rope[0]
    true_tail = rope[-1]
    visited = set()

    for motion in motions:
        direction, amount = motion

        for _ in range(amount):
            for k in range(knots - 1):
                head = rope[k]
                tail = rope[k + 1]

                if head == true_head: head.move(direction, 1)

                tail.follow(head)
                visited.add(true_tail.pos())

    return len(visited)


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Helpers
# └─────────────────────────────────────────────────────────────────────────────
def build_grid(motions: list[list[Any]]) -> str:
    """Go through the motions. Explore the Grid."""
    point = Point(0, 0, 'Marco Polo')
    x_min = y_min = 0
    x_max = y_max = 0

    for motion in motions:
        point.move(*motion)
        x_min = min(x_min, point.x)
        y_min = min(y_min, point.y)
        x_max = max(x_max, point.x)
        y_max = max(y_max, point.y)

    width = x_max - x_min + 1
    height = y_max - y_min + 1
    grid = f'{"·" * width}\n' * height
    return grid


def print_grid(grid: Any, points: list[Point] = []) -> None:
    """Visualize points on the Grid."""
    grid = [list(line) for line in grid.strip().split('\n')]

    for p in reversed(points):
        i, j, name = p.y, p.x, p.name
        grid[i][j] = name
    grid.reverse()

    grid = [''.join(line) for line in grid]
    grid = '\n'.join(grid) + '\n'
    print(grid)


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = count_tail_positions(X, knots=2)
P1 = count_tail_positions(P, knots=2)
prettyprint(X1, P1)

X2 = count_tail_positions(X, knots=10)
P2 = count_tail_positions(P, knots=10)
prettyprint(X2, P2)
