#!/usr/bin/env python3
"""https://leetcode.com/problems/circular-array-loop/"""

class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            slow = fast = i
            direction = nums[i] < 0
            while True:
                slow = self.next(nums, slow, direction)
                fast = self.next(nums, fast, direction)
                fast = self.next(nums, fast, direction)
                if slow == -1 or fast == -1: break
                if slow == fast: return True
        return False

    def next(self, nums: list[int], i: int, direction: bool) -> int:
        is_oob = i == -1
        is_diff_directions = (nums[i] < 0) != direction
        if is_oob or is_diff_directions: return -1

        i_next = (i + nums[i]) % len(nums)
        is_singleton = i_next == i

        return i_next if not is_singleton else -1


class SolutionAlt:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        seen_all, n = set(), len(nums)
        for i in range(n):
            if i not in seen_all:
                seen_temp = set()
                while True:
                    if i in seen_temp: return True
                    if i in seen_all: break
                    seen_temp.add(i)
                    seen_all.add(i)

                    prev, i = i, (i + nums[i]) % n
                    is_singleton = prev == i
                    is_diff_directions = (nums[prev] * nums[i]) < 0
                    if is_singleton or is_diff_directions: break
        return False
