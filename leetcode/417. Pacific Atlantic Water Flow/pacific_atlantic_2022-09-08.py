#!/usr/bin/env python3
"""https://leetcode.com/problems/pacific-atlantic-water-flow/"""

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        visited_pacific, visited_atlantic = set(), set()

        def _dfs(i, j, visited):
            if (i, j) in visited: return
            visited.add((i, j))

            deltas = ((0, 1), (0, -1), (-1, 0), (1, 0))
            for di, dj in deltas:
                i_next, j_next = i + di, j + dj
                is_in_bounds = (0 <= i_next < m) and (0 <= j_next < n)
                if is_in_bounds and heights[i_next][j_next] >= heights[i][j]:
                    _dfs(i_next, j_next, visited)

        for i in range(m):
            _dfs(i, 0, visited_pacific)
            _dfs(i, n - 1, visited_atlantic)
        for j in range(n):
            _dfs(0, j, visited_pacific)
            _dfs(m - 1, j, visited_atlantic)

        dual_riverheads = list(visited_pacific & visited_atlantic)
        return dual_riverheads
