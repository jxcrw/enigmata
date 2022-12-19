#!/usr/bin/env python3
"""https://leetcode.com/problems/find-smallest-letter-greater-than-target/"""

from bisect import bisect_right


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        i = self._bisect_right(letters, target)
        letter = letters[i % len(letters)]
        return letter

    def _bisect_right(self, letters: list[str], target: str) -> int:
        l, r = 0, len(letters) - 1
        while l <= r:
            m = (l + r) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m - 1
        return l


class SolutionAlt:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        i = bisect_right(letters, target)
        letter = letters[i % len(letters)]
        return letter
