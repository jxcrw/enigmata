#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-common-prefix/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n) * min string length / O(1)
    def longestCommonPrefix(self, strings: list[str]) -> str:
        prefix, i = "", 0
        while True:
            try:
                chars = {_[i] for _ in strings}
                if len(chars) != 1: break
                prefix += chars.pop()
                i += 1
            except IndexError:
                break
        return prefix

class SolutionPreferred:
    # Time / Space: O(n) * min string length / O(1)
    def longestCommonPrefix(self, strings: list[str]) -> str:
        prefix = ""
        for chars in zip(*strings):
            if len(set(chars)) != 1: break
            prefix += chars[0]
        return prefix


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: fl)
    strings = ["flower", "flow", "flight"]
    print(s_init.longestCommonPrefix(strings))
    print(s_pref.longestCommonPrefix(strings))

    # Example 2 (Expected Output: "")
    strings = ["dog", "racecar", "car"]
    print(s_init.longestCommonPrefix(strings))
    print(s_pref.longestCommonPrefix(strings))

    # Benchmarking
    number = 100_000
    strings = ["Lorem", "ipsum", "dolor", "sit", "amet,", "consectetur", "adipiscing", "elit.", "Cras", "sit", "amet", "elit", "vel", "risus", "accumsan", "luctus", "quis", "non", "orci.", "Cras."]
    print(timeit.timeit(lambda: s_init.longestCommonPrefix(strings), number=number))
    print(timeit.timeit(lambda: s_pref.longestCommonPrefix(strings), number=number))
