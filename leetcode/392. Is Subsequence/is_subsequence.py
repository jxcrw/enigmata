#!/usr/bin/env python3
"""https://leetcode.com/problems/is-subsequence/"""

import bisect
from collections import defaultdict
import timeit


class SolutionInitial:
    # Time / Space: O(|t|) / O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = pt = 0
        ns, nt = len(s), len(t)
        while ps < ns and pt < nt:
            if s[ps] == t[pt]: ps += 1
            pt += 1
        return ps == ns


class SolutionPreferred:
    # Time / Space: O(|t| + |s|·log(|t|)) / O(|t|)
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


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: True)
    s, t = 'abc', 'ahbgdc'
    print(s_init.isSubsequence(s,t))
    print(s_pref.isSubsequence(s,t))

    # Example 2 (Expected Output: False)
    s, t = 'axc', 'ahbgdcx'
    print(s_init.isSubsequence(s,t))
    print(s_pref.isSubsequence(s,t))

    # Benchmarking
    number = 100
    s, t = 'axc', '0' * 100_000 + 'ahbgdc'
    print(timeit.timeit(lambda: s_init.isSubsequence(s,t), number=number))
    print(timeit.timeit(lambda: s_pref.isSubsequence(s,t), number=number))
