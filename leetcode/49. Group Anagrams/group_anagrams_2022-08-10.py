#!/usr/bin/env python3
"""https://leetcode.com/problems/group-anagrams/"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            anagrams[s_sorted].append(s)
        return anagrams.values()
