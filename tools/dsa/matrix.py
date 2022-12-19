#!/usr/bin/env python3
"""Matrix stuff"""

from typing import Any


class Matrix:
    """A rectangular matrix. Backed by a Python list."""
    def __init__(self, data: list[list[Any]]):
        self.D = data
        self.T = self.transposed()

        m, n = len(data), len(data[0])
        self.m = m
        self.n = n
        self.area = m * n
        self.perimeter = 2 * m + 2 * n - 4 # -4 so corner elements only counted once

    def get(self, i: int, j: int) -> Any:
        """Get element (i, j)."""
        cell = self.D[i][j]
        return cell

    def look(self, direction: str, i: int, j: int) -> list[Any]:
        """Get the elements seen in the specified direction from the perspective of element (i, j)."""
        cells = []
        match direction:
            case 'L':
                cells = self.D[i][:j]
                cells.reverse()
            case 'R':
                if j < self.n - 1:
                    cells = self.D[i][j + 1:]
            case 'U':
                cells = self.T[j][:i]
                cells.reverse()
            case 'D':
                if i < self.m - 1:
                    cells = self.T[j][i + 1:]
            case _:
                raise Exception('Unsupported direction.')
        return cells

    def transposed(self) -> list[list[Any]]:
        """Make a transposed copy of the matrix."""
        t = [list(i) for i in zip(*self.D)]
        return t
