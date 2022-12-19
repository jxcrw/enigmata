#!/usr/bin/env python3
"""https://leetcode.com/problems/group-anagrams/"""

from collections import defaultdict
import timeit

class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        hashmap = {}
        for string in strings:
            string_sorted = ''.join(sorted(string))
            if string_sorted in hashmap:
                hashmap[string_sorted].append(string)
            else:
                hashmap[string_sorted] = [string]
        anagrams = list(hashmap.values())
        return anagrams

class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for string in strings:
            string_sorted = ''.join(sorted(string))
            hashmap[string_sorted].append(string)
        anagrams = list(hashmap.values())
        return anagrams


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s_init.groupAnagrams(strings))
    print(s_pref.groupAnagrams(strings))

    # Example 2 (Expected Output: [[""]])
    strings = [""]
    print(s_init.groupAnagrams(strings))
    print(s_pref.groupAnagrams(strings))

    # Example 2 (Expected Output: [["a"]])
    strings = ["a"]
    print(s_init.groupAnagrams(strings))
    print(s_pref.groupAnagrams(strings))

    # Benchmarking
    number = 10000
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(timeit.timeit(lambda: s_init.groupAnagrams(strings), number=number))
    print(timeit.timeit(lambda: s_pref.groupAnagrams(strings), number=number))
