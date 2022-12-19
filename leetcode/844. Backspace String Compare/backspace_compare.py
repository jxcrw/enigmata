#!/usr/bin/env python3
"""https://leetcode.com/problems/backspace-string-compare/"""

import itertools
import timeit

class SolutionInitial:
    # Time / Space: O(m + n), O(m + n)
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_built = self._build(s)
        t_built = self._build(t)
        return s_built == t_built

    def _build(self, string: str) -> str:
        stack = []
        for c in string:
            if c != '#': stack.append(c)
            elif stack: stack.pop()
        return ''.join(stack)

class SolutionAlternate:
    # Time / Space: O(n), O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_built = self._build(s)
        t_built = self._build(t)
        return s_built == t_built

    def _build(self, string: str):
        skip, built = 0, ''
        for c in reversed(string):
            if c == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                built += c
        return built

class SolutionPreferred:
    # Time / Space: O(n), O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_simulate, t_simulate = self._simulate(s), self._simulate(t)
        are_equal = all(x == y for x, y in itertools.zip_longest(s_simulate, t_simulate))
        return are_equal

    def _simulate(self, string: str):
        skip = 0
        for c in reversed(string):
            if c == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield c


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: true)
    s, t = 'ab#c', 'ad#c'
    print(s_init.backspaceCompare(s, t))
    print(s_alt.backspaceCompare(s, t))
    print(s_pref.backspaceCompare(s, t))

    # Example 2 (Expected Output: true)
    s, t = 'ab##', 'c#d#'
    print(s_init.backspaceCompare(s, t))
    print(s_alt.backspaceCompare(s, t))
    print(s_pref.backspaceCompare(s, t))

    # Example 3 (Expected Output: false)
    s, t = 'a#c', 'b'
    print(s_init.backspaceCompare(s, t))
    print(s_alt.backspaceCompare(s, t))
    print(s_pref.backspaceCompare(s, t))

    # Benchmarking
    number = 10_000
    big_mama = ''.join([v for pair in zip(['abc'] * 100, ['#'] * 100) for v in pair])
    s, t = big_mama, big_mama
    print(timeit.timeit(lambda: s_init.backspaceCompare(s, t), number=number))
    print(timeit.timeit(lambda: s_alt.backspaceCompare(s, t), number=number))
    print(timeit.timeit(lambda: s_pref.backspaceCompare(s, t), number=number))
