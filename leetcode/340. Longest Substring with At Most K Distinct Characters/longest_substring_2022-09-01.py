#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/"""

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            if len(counts) > k:
                counts[s[l]] -= 1
                if counts[s[l]] == 0: counts.pop(s[l])
                l += 1
        return r - l + 1
