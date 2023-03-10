#!/usr/bin/env python3
"""https://leetcode.com/problems/substring-with-concatenation-of-all-words/"""

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        start_indices, counter_orig = [], Counter(words)
        num_words, word_length = len(words), len(words[0])
        L, R = 0, num_words * word_length

        while R <= len(s):
            l, r = L, L + word_length
            trigger = s[l:r]

            if trigger in counter_orig:
                counter_temp = Counter()
                matches_needed = len(counter_orig)

                while r <= R:
                    substring = s[l:r]
                    counter_temp[substring] += 1
                    count_temp, count_orig = counter_temp[substring], counter_orig[substring]

                    if count_temp > count_orig: break
                    if count_temp == count_orig: matches_needed -= 1
                    if matches_needed == 0: start_indices.append(L)

                    l += word_length
                    r += word_length
            L += 1
            R += 1

        return start_indices
