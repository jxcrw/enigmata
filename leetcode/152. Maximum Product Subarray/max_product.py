#!/usr/bin/env python3
"""https://leetcode.com/problems/maximum-product-subarray/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def maxProduct(self, numbers: list[int]) -> int:
        max_current = min_current = max_final = numbers[0]
        for number in numbers[1:]:
            max_temp = max(number, max_current * number, min_current * number)
            min_current = min(number, max_current * number, min_current * number)
            max_current = max_temp
            max_final = max(max_current, max_final)
        return max_final

class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def maxProduct(self, numbers: list[int]) -> int:
        max_current, min_current, max_final = 1, 1, -float('inf')
        for n in numbers:
            x = max_current * n
            y = min_current * n
            min_current = min(n, x, y)
            max_current = max(n, x, y)
            max_final = max(max_current, max_final)
        return max_final


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 6)
    numbers = [2, 3, -2, 4]
    print(s_init.maxProduct(numbers))
    print(s_pref.maxProduct(numbers))

    # Example 2 (Expected Output: 0)
    numbers = [-2, 0, -1]
    print(s_init.maxProduct(numbers))
    print(s_pref.maxProduct(numbers))

    # Example 3 (Expected Output: 24)
    numbers = [-2, 3, -4]
    print(s_init.maxProduct(numbers))
    print(s_pref.maxProduct(numbers))

    # Example 4 (Expected Output: 12)
    numbers = [-4, -3, -2]
    print(s_init.maxProduct(numbers))
    print(s_pref.maxProduct(numbers))

    # Benchmarking
    numbers = list(range(1000))
    print(timeit.timeit(lambda: s_init.maxProduct(numbers), number=1000))
    print(timeit.timeit(lambda: s_pref.maxProduct(numbers), number=1000))

