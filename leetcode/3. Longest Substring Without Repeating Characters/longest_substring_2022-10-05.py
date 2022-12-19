#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-substring-without-repeating-characters/"""

class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        prev_use_indices = {}
        length_max = 0
        l = 0
        for r, c in enumerate(string):
            if c in prev_use_indices and prev_use_indices[c] >= l:
                l = prev_use_indices[c] + 1
            else:
                length_max = max(length_max, r - l + 1)
            prev_use_indices[c] = r
        return length_max
