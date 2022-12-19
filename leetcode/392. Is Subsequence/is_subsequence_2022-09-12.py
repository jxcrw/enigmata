#!/usr/bin/env python3
"""https://leetcode.com/problems/is-subsequence/"""

import bisect
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = pt = 0
        ns, nt = len(s), len(t)
        while ps < ns and pt < nt:
            if s[ps] == t[pt]: ps += 1
            pt += 1
        return ps == ns


class SolutionAlternate:
    def isSubsequence(self, s: str, t: str) -> bool:
        letter_indices = defaultdict(list)
        for i, c in enumerate(t):
            letter_indices[c].append(i)

        i_curr = -1
        for c in s:
            if c not in letter_indices: return False

            indices = letter_indices[c]
            i_match = bisect.bisect_right(indices, i_curr)
            if i_match != len(indices):
                i_curr = indices[i_match]
            else:
                return False

        return True
