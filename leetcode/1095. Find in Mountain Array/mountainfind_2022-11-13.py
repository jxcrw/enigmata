#!/usr/bin/env python3
"""https://leetcode.com/problems/find-in-mountain-array/"""

from tools.dsa._leetcode import MountainArray


class Solution:
    def findInMountainArray(self, target: int, array: MountainArray) -> int:
        n = array.length()

        # Find peak
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if array.get(m) < array.get(m + 1):
                l = m + 1
            else:
                r = m - 1
        i_peak = l

        # Search ascent
        l, r = 0, i_peak
        while l <= r:
            m = (l + r) // 2
            m_val = array.get(m)
            if m_val < target:
                l = m + 1
            elif m_val > target:
                r = m - 1
            else:
                return m

        # Search descent
        l, r = i_peak, n - 1
        while l <= r:
            m = (l + r) // 2
            m_val = array.get(m)
            if m_val > target:
                l = m + 1
            elif m_val < target:
                r = m - 1
            else:
                return m

        return -1
