#!/usr/bin/env python3
"""https://leetcode.com/problems/container-with-most-water/"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        area_max = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area_max = max(area_max, width * height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area_max
