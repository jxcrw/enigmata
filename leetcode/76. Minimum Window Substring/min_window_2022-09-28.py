#!/usr/bin/env python3
"""https://leetcode.com/problems/minimum-window-substring/"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substring = ''
        counter = Counter(t)
        matches_needed = len(counter)

        l = 0
        for r in range(len(s)):
            counter[s[r]] -= 1
            if counter[s[r]] == 0: matches_needed -= 1

            while matches_needed == 0:
                len_window = r - l + 1
                if not substring or len_window < len(substring):
                    substring = s[l:r + 1]

                counter[s[l]] += 1
                if counter[s[l]] > 0: matches_needed += 1
                l += 1

        return substring
