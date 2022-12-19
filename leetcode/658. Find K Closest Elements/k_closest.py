#!/usr/bin/env python3
"""https://leetcode.com/problems/find-k-closest-elements/"""

import timeit


class Solution:
    # Time / Space: O(log(n - k) + k) / O(1)
    def findClosestElements(self, nums: list[int], k: int, target: int) -> list[int]:
        l, r = 0, len(nums) - k - 1

        while l <= r:
            m = (l + r) // 2
            if target - nums[m] > nums[m + k] - target:
                l = m + 1
            else:
                r = m - 1

        return nums[l:l + k]


if __name__ == '__main__':
    s_init = Solution()

    # Example 0 (Expected Output: [1, 2, 3, 4])
    nums, k, target = [1, 2, 3, 4, 5], 4, 3
    print(s_init.findClosestElements(nums, k, target))

    # Example 1 (Expected Output: [1, 2, 3, 4])
    nums, k, target = [1, 2, 3, 4, 5], 4, -1
    print(s_init.findClosestElements(nums, k, target))

    # Benchmarking
    number = 10_000
    nums, k, target = list(range(10_000)), 5, 5000
    print(timeit.timeit(lambda: s_init.findClosestElements(nums, k, target), number=number))
