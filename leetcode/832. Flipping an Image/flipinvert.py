#!/usr/bin/env python3
"""https://leetcode.com/problems/flipping-an-image/"""

from copy import deepcopy
import timeit


class SolutionInitial:
    # Time / Space: O(|image|) / O(1)
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            image[i].reverse()
            image[i] = [x ^ 1 for x in image[i]]
        return image


class SolutionPreferred:
    # Time / Space: O(|image|) / O(1)
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n_halfrow = (len(image[0]) + 1) // 2
        for row in image:
            for i in range(n_halfrow):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return image


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [[1, 0, 0], [0, 1, 0], [1, 1, 1]])
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(s_init.flipAndInvertImage(deepcopy(image)))
    print(s_pref.flipAndInvertImage(deepcopy(image)))

    # Example 2 (Expected Output: [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]])
    image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    print(s_init.flipAndInvertImage(deepcopy(image)))
    print(s_pref.flipAndInvertImage(deepcopy(image)))

    # Benchmarking
    number = 100
    row = [0] * 500
    image = [row for i in range(500)]
    print(timeit.timeit(lambda: s_init.flipAndInvertImage(deepcopy(image)), number=number))
    print(timeit.timeit(lambda: s_pref.flipAndInvertImage(deepcopy(image)), number=number))
