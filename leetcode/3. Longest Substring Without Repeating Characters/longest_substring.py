#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-substring-without-repeating-characters/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n^2) / O(n)
    def lengthOfLongestSubstring(self, string: str) -> int:
        candidates, n = [], len(string)
        if n in [0, 1]: return n

        for i in range(n):
            candidate = string[i]
            for j in range(i + 1, n):
                if string[j] not in candidate:
                    candidate += string[j]
                else:
                    break
            candidates.append(candidate)
        lengths = [len(_) for _ in candidates]
        length_max = max(lengths)
        return length_max

class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def lengthOfLongestSubstring(self, string: str) -> tuple[int, str]:
        char_indexes = {}
        left = length_max = dirty = 0
        for right, c in enumerate(string):
            if c in char_indexes and left <= char_indexes[c]:
                left = char_indexes[c] + 1
            else:
                length_max = max(length_max, right - left + 1)
                if length_max != dirty:
                    dirty = length_max
                    substring = string[left:right + 1]
            char_indexes[c] = right
        return (length_max, substring)


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 3)
    string = "tuvtuvuu"
    print(s_init.lengthOfLongestSubstring(string))
    print(s_pref.lengthOfLongestSubstring(string))

    # Example 2 (Expected Output: 1)
    string = "bbbbb"
    print(s_init.lengthOfLongestSubstring(string))
    print(s_pref.lengthOfLongestSubstring(string))

    # Example 3 (Expected Output: 3)
    string = "pwwkew"
    print(s_init.lengthOfLongestSubstring(string))
    print(s_pref.lengthOfLongestSubstring(string))

    # Example 4 (Expected Output: 1)
    string = " "
    print(s_init.lengthOfLongestSubstring(string))
    print(s_pref.lengthOfLongestSubstring(string))

    # Benchmarking
    number = 10_000
    string = "abcabcbb"
    print(timeit.timeit(lambda: s_init.lengthOfLongestSubstring(string), number=number))
    print(timeit.timeit(lambda: s_pref.lengthOfLongestSubstring(string), number=number))
