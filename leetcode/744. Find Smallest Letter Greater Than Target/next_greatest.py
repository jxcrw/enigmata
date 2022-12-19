#!/usr/bin/env python3
"""https://leetcode.com/problems/find-smallest-letter-greater-than-target/"""

from bisect import bisect
import timeit


class SolutionInitial:
    # Time / Space: O(n) / O(1)
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]


class SolutionAlternate:
    # Time / Space: O(log n) / O(1)
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        i = bisect(letters, target)
        letter = letters[i % len(letters)]
        return letter


class SolutionPreferred:
    # Time / Space: O(log n) / O(1)
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m - 1

        letter = letters[l % n]
        return letter


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()
    s_pref = SolutionPreferred()

    # Example 0 (Expected Output: 'c')
    letters, target = ['c', 'f', 'j'], 'a'
    print(s_init.nextGreatestLetter(letters, target))
    print(s_alt.nextGreatestLetter(letters, target))
    print(s_pref.nextGreatestLetter(letters, target))

    # Example 1 (Expected Output: 'f')
    letters, target = ['c', 'f', 'j'], 'c'
    print(s_init.nextGreatestLetter(letters, target))
    print(s_alt.nextGreatestLetter(letters, target))
    print(s_pref.nextGreatestLetter(letters, target))

    # Example 2 (Expected Output: 'x')
    letters, target = ['x', 'x', 'y', 'y'], 'z'
    print(s_init.nextGreatestLetter(letters, target))
    print(s_alt.nextGreatestLetter(letters, target))
    print(s_pref.nextGreatestLetter(letters, target))

    # Benchmarking
    number = 1_000
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters = []
    for c in alphabet: letters.extend([c] * 1000)
    target = 'o'
    print(timeit.timeit(lambda: s_init.nextGreatestLetter(letters, target), number=number))
    print(timeit.timeit(lambda: s_alt.nextGreatestLetter(letters, target), number=number))
    print(timeit.timeit(lambda: s_pref.nextGreatestLetter(letters, target), number=number))
