#!/usr/bin/env python3
"""https://leetcode.com/problems/product-of-array-except-self/"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        products = [1] * n

        product_left = 1
        for i in range(n):
            products[i] *= product_left
            product_left *= nums[i]

        product_right = 1
        for i in reversed(range(n)):
            products[i] *= product_right
            product_right *= nums[i]

        return products
