#!/usr/bin/env python3
"""https://leetcode.com/problems/palindrome-number/"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        string_rev = string[::-1]
        return string == string_rev


class SolutionAlternate:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        rev, n = 0, x
        while n:
            ones = n % 10
            rev = rev * 10 + ones
            n //= 10
        return rev == x
