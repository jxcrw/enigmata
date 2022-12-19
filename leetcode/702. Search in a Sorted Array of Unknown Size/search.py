#!/usr/bin/env python3
"""https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/"""

import timeit

from tools.dsa._leetcode import ArrayReader


class SolutionInitial:
    # Time / Space: O(log n) / O(1)
    def search(self, reader: ArrayReader | None, target: int) -> int:
        n = self.get_array_length(reader)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            m_val = reader.get(m)
            if m_val < target: l = m + 1
            elif m_val > target: r = m - 1
            else: return m
        return -1

    def get_array_length(self, reader: ArrayReader | None) -> int:
        max_length, oob = 10 ** 4, 2 ** 31 - 1
        l, r = 0, max_length
        while l <= r:
            m = (l + r) // 2
            val = reader.get(m)
            if val == oob:
                r = m - 1
            else:
                l = m + 1
        return r


class SolutionPreferred:
    # Time / Space: O(log n) / O(1)
    def search(self, reader: ArrayReader | None, target: int) -> int:
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


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 0 (Expected Output: 4)
    secret, target = ArrayReader([-1, 0, 3, 5, 9, 12]), 9
    # print(s_init.search(secret, target))
    print(s_pref.search(secret, target))

    # Example 1 (Expected Output: -1)
    secret, target = ArrayReader([-1, 0, 3, 5, 9, 12]), 2
    # print(s_init.search(secret, target))
    print(s_pref.search(secret, target))

    # Benchmarking
    number = 10_000
    secret, target = ArrayReader([-1, 0, 3, 5, 9, 12]), 2
    # print(timeit.timeit(lambda: s_init.search(secret, target), number=number))
    print(timeit.timeit(lambda: s_pref.search(secret, target), number=number))
