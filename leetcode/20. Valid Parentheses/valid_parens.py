#!/usr/bin/env python3
"""https://leetcode.com/problems/valid-parentheses/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n) / O(1)
    def isValid(self, string: str) -> bool:
        length = len(string)
        valid_subs = ['()', '[]', '{}']
        while length > 0:
            for sub in valid_subs:
                string = string.replace(sub, '')
            length_new = len(string)
            if length_new == length:
                return False
            else:
                length = length_new
        return True

class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def isValid(self, string: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in string:
            if c in brackets:
                stack.append(c)
            elif not stack or c != brackets[stack.pop()]:
                return False
        return not stack


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: True)
    s = "()"
    print(s_init.isValid(s))
    print(s_pref.isValid(s))

    # Example 2 (Expected Output: True)
    s = "()[]{}"
    print(s_init.isValid(s))
    print(s_pref.isValid(s))

    # Example 3 (Expected Output: False)
    s = "(]"
    print(s_init.isValid(s))
    print(s_pref.isValid(s))

    # Benchmarking
    s = "(]"
    print(timeit.timeit(lambda: s_init.isValid(s), number=100_000))
    print(timeit.timeit(lambda: s_pref.isValid(s), number=100_000))
