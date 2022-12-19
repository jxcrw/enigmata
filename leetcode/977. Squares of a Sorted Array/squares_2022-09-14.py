#!/usr/bin/env python3
"""https://leetcode.com/problems/squares-of-a-sorted-array/"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        squares = [0] * n
        l, r = 0, n - 1
        while l <= r:
            square_l, square_r = nums[l] ** 2, nums[r] ** 2
            if square_l > square_r:
                squares[r - l] = square_l
                l += 1
            else:
                squares[r - l] = square_r
                r -= 1
        return squares
