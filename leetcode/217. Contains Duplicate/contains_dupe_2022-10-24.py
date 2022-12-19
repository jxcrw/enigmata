#!/usr/bin/env python3
"""https://leetcode.com/problems/contains-duplicate/"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n_list = len(nums)
        n_set = len(set(nums))
        return n_list > n_set
