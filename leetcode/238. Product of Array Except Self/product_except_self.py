#!/usr/bin/env python3
"""https://leetcode.com/problems/product-of-array-except-self/"""

import math
import timeit

class SolutionInitial:
    # Time / Space: O(n^2) / O(n)
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        products = []
        for i, number in enumerate(numbers):
            temp = numbers[:]
            temp.pop(i)
            product = math.prod(temp)
            products.append(product)
        return products

class SolutionAlternate:
    # Time / Space: O(n) / O(1)
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        n = len(numbers)
        lefts, rights, products = [0]*n, [0]*n, [0]*n

        lefts[0] = 1
        for i in range(1, n):
            lefts[i] = lefts[i - 1] * numbers[i - 1]

        rights[-1] = 1
        for i in reversed(range(n - 1)):
            rights[i] = rights[i + 1] * numbers[i + 1]

        products = [left * right for left, right in zip(lefts, rights)]
        return products

class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        # Set up for ensuing traversals and calculations.
        n = len(numbers)
        products = [1] * n

        # Traverse left to right, calculating left (prefix) products.
        left_product = 1
        for i in range(n):
            products[i] *= left_product
            left_product *= numbers[i]

        # Traverse right to left, calculating right (suffix) products on the fly,
        # and multiply with corresponding left products.
        right_product = 1
        for i in reversed(range(n)):
            products[i] *= right_product
            right_product *= numbers[i]

        return products


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [24, 12, 8, 6])
    numbers = [1, 2, 3, 4]
    print(s_init.productExceptSelf(numbers))
    print(s_alt.productExceptSelf(numbers))
    print(s_pref.productExceptSelf(numbers))

    # Example 2 (Expected Output: [0, 0, 9, 0, 0])
    numbers = [-1, 1, 0, -3, 3]
    print(s_init.productExceptSelf(numbers))
    print(s_alt.productExceptSelf(numbers))
    print(s_pref.productExceptSelf(numbers))

    # Benchmarking
    numbers = list(range(1_000))
    print(timeit.timeit(lambda: s_init.productExceptSelf(numbers), number=100))
    print(timeit.timeit(lambda: s_alt.productExceptSelf(numbers), number=100)) # ≈12x faster
    print(timeit.timeit(lambda: s_pref.productExceptSelf(numbers), number=100)) # ≈2x faster
