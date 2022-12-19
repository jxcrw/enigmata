#!/usr/bin/env python3
"""https://leetcode.com/problems/pacific-atlantic-water-flow/"""

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        seen_pacific, seen_atlantic = set(), set()
        m, n = len(heights), len(heights[0])

        def _dfs(i: int, j: int, seen: set[tuple[int, int]]):
            if (i, j) in seen: return
            seen.add((i, j))

            deltas = ((0, 1), (0, -1), (-1, 0), (1, 0))
            for di, dj in deltas:
                i_next, j_next = i + di, j + dj
                is_in_bounds = (0 <= i_next < m) and (0 <= j_next < n)
                if is_in_bounds and heights[i_next][j_next] >= heights[i][j]:
                    _dfs(i_next, j_next, seen)

        for i in range(m):
            _dfs(i, 0, seen_pacific)
            _dfs(i, n - 1, seen_atlantic)
        for j in range(n):
            _dfs(0, j, seen_pacific)
            _dfs(m - 1, j, seen_atlantic)

        dual_riverheads = list(seen_pacific & seen_atlantic)
        return dual_riverheads
