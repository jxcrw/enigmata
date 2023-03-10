#!/usr/bin/env python3
"""https://leetcode.com/problems/contains-duplicate/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def containsDuplicate(self, numbers: list[int]) -> bool:
        hashmap = {}
        for n in numbers:
            if n in hashmap:
                return True
            hashmap[n] = 'seen'
        return False

class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def containsDuplicate(self, numbers: list[int]) -> bool:
        length_list = len(numbers)
        length_set = len(set(numbers))
        return length_list > length_set


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: True)
    numbers = [1, 2, 3, 1]
    print(s_init.containsDuplicate(numbers))
    print(s_pref.containsDuplicate(numbers))

    # Example 2 (Expected Output: False)
    numbers = [1, 2, 3, 4]
    print(s_init.containsDuplicate(numbers))
    print(s_pref.containsDuplicate(numbers))

    # Example 3 (Expected Output: True)
    numbers = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(s_init.containsDuplicate(numbers))
    print(s_pref.containsDuplicate(numbers))

    # Benchmarking
    numbers = list(range(100_000))
    print(timeit.timeit(lambda: s_init.containsDuplicate(numbers), number=100))
    print(timeit.timeit(lambda: s_pref.containsDuplicate(numbers), number=100)) # ≈4x faster
