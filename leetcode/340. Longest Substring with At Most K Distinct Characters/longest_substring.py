#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/"""

import timeit
from collections import defaultdict

class SolutionInitial:
    # Time / Space: O(n) / O(k)
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i, counts = 0, defaultdict(int)
        for j in range(len(s)):
            counts[s[j]] += 1
            if len(counts) > k:
                counts[s[i]] -= 1
                if counts[s[i]] == 0: counts.pop(s[i])
                i += 1
        return j - i + 1


if __name__ == '__main__':
    s_init = SolutionInitial()

    # Example 1 (Expected Output: 3)
    s, k = 'eceba', 2
    print(s_init.lengthOfLongestSubstringKDistinct(s, k))

    # Example 2 (Expected Output: 2)
    s, k = 'aa', 1
    print(s_init.lengthOfLongestSubstringKDistinct(s, k))

    # Example 3 (Expected Output: 4)
    s, k = 'abcdddabceeeeeeee', 2
    print(s_init.lengthOfLongestSubstringKDistinct(s, k))

    # Benchmarking
    number = 10_000
    s, k = 'eceba', 2
    print(timeit.timeit(lambda: s_init.lengthOfLongestSubstringKDistinct(s, k), number=number))
