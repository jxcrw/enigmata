#!/usr/bin/env python3
"""Common tools and utility functions"""

from itertools import zip_longest
from typing import Any


def chunk(iterable, n: int, fillvalue=None):
    """Split iterable up into chunks of length n, with optional padding."""
    chunks = zip_longest(*[iter(iterable)] * n, fillvalue=fillvalue)
    chunks = list(chunks)
    return chunks


def transpose(matrix: list[list[Any]]) -> list[list[Any]]:
    """Transpose matrix, filling with ' ' where necessary."""
    matrix = [list(i) for i in zip_longest(*matrix, fillvalue=' ')]
    return matrix
