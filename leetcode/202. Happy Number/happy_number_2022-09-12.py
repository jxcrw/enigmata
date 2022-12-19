#!/usr/bin/env python3
"""https://leetcode.com/problems/happy-number/"""


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = squaresum(slow)
            fast = squaresum(squaresum(fast))
            if fast == 1: return True
            if slow == fast: return False


class SolutionAlternate:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            n = squaresum(n)
            if n == 1: return True
            if n in seen: return False
            seen.add(n)


def squaresum(n: int) -> int:
    r = 0
    while n:
        digit = n % 10
        r += digit ** 2
        n //= 10
    return r
