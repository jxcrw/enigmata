#!/usr/bin/env python3
"""https://leetcode.com/problems/complement-of-base-10-integer/"""

from math import floor, log2


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        bitlength = floor(log2(n)) + 1
        bitlength = n.bit_length()
        all_ones = (1 << bitlength) - 1
        complement = n ^ all_ones
        return complement
