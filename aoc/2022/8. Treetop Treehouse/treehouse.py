#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/8"""

from collections import deque
from typing import Any

from tools.aoc import load, prettyprint, superparse

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=0)
P, _ = load('_puzzle.txt', pre=0)

seps = deque(['\n', 'char'])
args = {'seps': seps, 'str_to_num': 'int', 'extract_num': False}
X = superparse(X, **args)
P = superparse(P, **args)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ New Features
# └─────────────────────────────────────────────────────────────────────────────
class Matrix:
    """A rectangular matrix. Backed by a Python list."""
    def __init__(self, data: list[list[Any]]):
        self.data = data
        self.data_T = self.transposed()

        m, n = len(data), len(data[0])
        self.m = m
        self.n = n
        self.area = m * n
        self.perimeter = 2 * m + 2 * n - 4 # -4 so corner elements only counted once

    def get(self, i: int, j: int) -> Any:
        """Get element (i, j)."""
        cell = self.data[i][j]
        return cell

    def look(self, direction: str, i: int, j: int) -> list[Any]:
        """Get the elements seen in the specified direction from the perspective of element (i, j)."""
        cells = []
        match direction:
            case 'L':
                cells = self.data[i][:j]
                cells.reverse()
            case 'R':
                if j < self.n - 1:
                    cells = self.data[i][j + 1:]
            case 'U':
                cells = self.data_T[j][:i]
                cells.reverse()
            case 'D':
                if i < self.m - 1:
                    cells = self.data_T[j][i + 1:]
            case _:
                raise Exception('Unsupported direction.')
        return cells

    def transposed(self) -> list[list[Any]]:
        """Make a transposed copy of the matrix."""
        t = [list(i) for i in zip(*self.data)]
        return t


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def count_visible_trees(height_map: list[list[int]]) -> int:
    """Count how many trees are visible in a map of tree heights."""
    forest = Matrix(height_map)
    count, m, n = 0, forest.m, forest.n

    for i in range(m):
        for j in range(n):
            tree = (i, j)
            if is_visible(tree, forest):
                count += 1
    return count


def is_visible(tree: tuple[int, int], forest: Matrix) -> bool:
    """Determine whether the ij-th tree in the forest is visible."""
    my_height = forest.get(*tree)
    for direction in ('L', 'R', 'U', 'D'):
        heights = forest.look(direction, *tree)
        visible = all(h < my_height for h in heights) # Note: True by default when heights = [] (along edges)
        if visible: return True
    return False


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
def max_scenic_score(height_map: list[list[int]]) -> float:
    """Find the max scenic score of any tree in the map of tree heights."""
    forest = Matrix(height_map)
    max_score, m, n = -float('inf'), forest.m, forest.n

    for i in range(m):
        for j in range(n):
            tree = (i, j)
            score = calc_scenic_score(tree, forest)
            max_score = max(max_score, score)
    return max_score


def calc_scenic_score(tree: tuple[int, int], forest: Matrix) -> int:
    """Compute the scenic score of a tree in the forest."""
    score = 1
    my_height = forest.get(*tree)

    for direction in ('L', 'R', 'U', 'D'):
        view = 0
        heights = forest.look(direction, *tree)

        for h in heights:
            view += 1
            if h >= my_height: break
        score *= view
    return score


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = count_visible_trees(X)
P1 = count_visible_trees(P)
prettyprint(X1, P1)

X2 = max_scenic_score(X)
P2 = max_scenic_score(P)
prettyprint(X2, P2)
