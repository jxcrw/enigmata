#!/usr/bin/env python3
"""https://leetcode.com/problems/number-complement/"""

import timeit


class SolutionInitial:
    # Time / Space: O(1) / O(1)
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        todo, bit = n, 1
        while todo:
            n ^= bit
            bit <<= 1
            todo >>= 1
        return n


class SolutionAlternate:
    # Time / Space: O(1) / O(1)
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        bitmask = n
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        return bitmask ^ n


class SolutionPreferred:
    # Time / Space: O(1) / O(1)
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        # bitlength = floor(log2(n)) + 1
        bitlength = n.bit_length()
        all_ones = (1 << bitlength) - 1
        return all_ones ^ n


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 2)
    n = 5
    print(s_init.bitwiseComplement(n))
    print(s_alt.bitwiseComplement(n))
    print(s_pref.bitwiseComplement(n))

    # Example 2 (Expected Output: 0)
    n = 7
    print(s_init.bitwiseComplement(n))
    print(s_alt.bitwiseComplement(n))
    print(s_pref.bitwiseComplement(n))

    # Example 3 (Expected Output: 5)
    n = 10
    print(s_init.bitwiseComplement(n))
    print(s_alt.bitwiseComplement(n))
    print(s_pref.bitwiseComplement(n))

    # Benchmarking
    number = 500
    n = number ** number
    print(timeit.timeit(lambda: s_init.bitwiseComplement(n), number=number))
    print(timeit.timeit(lambda: s_alt.bitwiseComplement(n), number=number))
    print(timeit.timeit(lambda: s_pref.bitwiseComplement(n), number=number))
