#!/usr/bin/env python3
"""https://leetcode.com/problems/fruit-into-baskets/"""

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        counts = defaultdict(int)
        l = 0
        for r in range(len(fruits)):
            counts[fruits[r]] += 1
            if len(counts) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0: counts.pop(fruits[l])
                l += 1
        return r - l + 1
