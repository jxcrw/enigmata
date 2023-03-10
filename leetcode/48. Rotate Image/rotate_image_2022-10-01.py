#!/usr/bin/env python3
"""https://leetcode.com/problems/rotate-image/"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        matrix.reverse()
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
