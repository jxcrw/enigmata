#!/usr/bin/env python3
"""https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/"""

from tools.dsa._leetcode import ArrayReader


class Solution:
    def search(self, reader: ArrayReader, target: int) -> int:
        l, r = 0, 1
        while reader.get(r) < target:
            l = r
            r *= 2

        while l <= r:
            m = (l + r) // 2
            m_val = reader.get(m)
            if m_val < target: l = m + 1
            elif m_val > target: r = m - 1
            else: return m
        return -1
