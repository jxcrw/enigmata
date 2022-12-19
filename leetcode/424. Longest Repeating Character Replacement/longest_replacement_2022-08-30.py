#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-repeating-character-replacement/"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs, freq_max = defaultdict(int), 0
        l = 0
        for r in range(len(s)):
            freqs[s[r]] += 1
            freq_max = max(freq_max, freqs[s[r]])
            if r - l + 1 - freq_max > k:
                freqs[s[l]] -= 1
                l += 1
        return r - l + 1
