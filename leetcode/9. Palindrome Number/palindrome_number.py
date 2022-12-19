#!/usr/bin/env python3
"""https://leetcode.com/problems/palindrome-number/"""

import timeit

class SolutionInitial:
    # Time / Space: O(1)ish / O(1)
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        string_reversed = string[::-1]
        return string == string_reversed

class SolutionAlternate:
    # Time / Space: O(n)ish / O(1)
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        n, rev = x, 0
        while n:
            last_digit = n % 10
            rev = rev * 10 + last_digit
            n //= 10
        return x == rev


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()

    # Example 1 (Expected Output: True)
    x = 121
    print(s_init.isPalindrome(x))
    print(s_alt.isPalindrome(x))

    # Example 2 (Expected Output: False)
    x = -121
    print(s_init.isPalindrome(x))
    print(s_alt.isPalindrome(x))

    # Example 3 (Expected Output: False)
    x = 10
    print(s_init.isPalindrome(x))
    print(s_alt.isPalindrome(x))

    # Benchmarking
    number = 100_000
    x = 12345612356478956152345678994512345678912364567894561235678945671235689456234578456
    print(timeit.timeit(lambda: s_init.isPalindrome(x), number=number))
    print(timeit.timeit(lambda: s_alt.isPalindrome(x), number=number))
