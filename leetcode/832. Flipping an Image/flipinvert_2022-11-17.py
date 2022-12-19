#!/usr/bin/env python3
"""https://leetcode.com/problems/flipping-an-image/"""

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n_halfrow = (len(image[0]) + 1) // 2
        for row in image:
            for i in range(n_halfrow):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return image
