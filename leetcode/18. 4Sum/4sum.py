#!/usr/bin/env python3
"""https://leetcode.com/problems/4sum/"""

import timeit


class Solution:
    # Time / Space: O(n^(k-1)) / O(n) (for recursion) where n = k
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        return self._k_sum(nums, target, 4)

    def _k_sum(self, nums: list[int], target: int, k: int) -> list[list[int]]:
        res = []
        if not nums: return res

        average = target // k
        if average < nums[0] or average > nums[-1]: return res

        if k == 2: return self._two_sum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                for subset in self._k_sum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)

        return res

    def _two_sum(self, nums: list[int], target: int) -> list[list[int]]:
        res, n = [], len(nums)
        l, r = 0, n - 1
        while l < r:
            total = nums[l] + nums[r]
            if total < target or (l > 0 and nums[l] == nums[l - 1]):
                l += 1
            elif total > target or (r < n - 1 and nums[r] == nums[r + 1]):
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
        return res


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    nums, target = [1, 0, -1, 0, -2, 2], 0
    print(solution.fourSum(nums, target))

    # Example 2 (Expected Output: [[2, 2, 2, 2]])
    nums, target = [2, 2, 2, 2, 2], 8
    print(solution.fourSum(nums, target))

    # Benchmarking
    number = 10_000
    nums, target = [2, 2, 2, 2, 2], 8
    print(timeit.timeit(lambda: solution.fourSum(nums, target), number=number))
