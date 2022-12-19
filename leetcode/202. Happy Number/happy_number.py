#!/usr/bin/env python3
"""https://leetcode.com/problems/happy-number/"""

import timeit


class SolutionInitial:
    # Time / Space: O(log n) / O(log n)
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            n = squaresum(n)
            if n == 1: return True
            if n in seen: return False
            seen.add(n)


class SolutionAlternate:
    # Time / Space: O(log n) / O(1)
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = squaresum(slow)
            fast = squaresum(squaresum(fast))
            if fast == 1: return True
            if slow == fast: return False


def squaresum(n: int) -> int:
    r = 0
    while n:
        digit = n % 10
        r += digit ** 2
        n //= 10
    return r


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()

    # Example 1 (Expected Output: True)
    n = 19
    print(s_init.isHappy(n))
    print(s_alt.isHappy(n))

    # Example 2 (Expected Output: False)
    n = 2
    print(s_init.isHappy(n))
    print(s_alt.isHappy(n))

    # Benchmarking
    number = 10_000
    n = 123_456_789_123_456_789
    print(timeit.timeit(lambda: s_init.isHappy(n), number=number))
    print(timeit.timeit(lambda: s_alt.isHappy(n), number=number))
