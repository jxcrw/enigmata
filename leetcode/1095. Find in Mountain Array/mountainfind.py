#!/usr/bin/env python3
"""https://leetcode.com/problems/find-in-mountain-array/"""

import timeit

from tools.dsa._leetcode import MountainArray


class SolutionInitial:
    # Time / Space: O(log n) / O(1)
    def findInMountainArray(self, target: int, array: MountainArray) -> int:
        n = array.length()

        # Find peak index
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            is_ascending = array.get(m) < array.get(m + 1)
            if is_ascending: l = m + 1
            else: r = m - 1
        i_peak = l

        # Search ascent
        l, r = 0, i_peak
        while l <= r:
            m = (l + r) // 2
            if array.get(m) < target: l = m + 1
            elif array.get(m) > target: r = m - 1
            else: return m

        # Search descent
        l, r = i_peak, n - 1
        while l <= r:
            m = (l + r) // 2
            if array.get(m) > target: l = m + 1
            elif array.get(m) < target: r = m - 1
            else: return m

        return -1


if __name__ == '__main__':
    s_init = SolutionInitial()

    # Example 0 (Expected Output: 2)
    array, target = MountainArray([1, 2, 3, 4, 5, 3, 1]), 3
    print(s_init.findInMountainArray(target, array))

    # Example 1 (Expected Output: -1)
    array, target = MountainArray([0, 1, 2, 4, 2, 1]), 3
    print(s_init.findInMountainArray(target, array))

    # Benchmarking
    number = 10_000
    array, target = MountainArray(list(range(100_000)) + [100_000] + list(reversed(range(50_000)))), 50_000
    print(timeit.timeit(lambda: s_init.findInMountainArray(target, array), number=number))
