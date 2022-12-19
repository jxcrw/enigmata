#!/usr/bin/env python3
"""https://leetcode.com/problems/circular-array-loop/"""

import timeit


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n, seen_all = len(nums), set()
        for i in range(n):
            if i not in seen_all:
                seen_temp = set()
                while True:
                    if i in seen_temp: return True
                    if i in seen_all: break
                    seen_temp.add(i)
                    seen_all.add(i)

                    prev, i = i, (i + nums[i]) % n
                    is_singleton = i == prev
                    is_diff_directions = nums[i] * nums[prev] < 0
                    if is_singleton or is_diff_directions: break
        return False


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def circularArrayLoop(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            slow = fast = i
            direction = nums[i] > 0

            while True:
                slow = self._next(nums, slow, direction)
                fast = self._next(nums, fast, direction)
                fast = self._next(nums, fast, direction)
                if slow == -1 or fast == -1: break
                elif slow == fast: return True
        return False

    def _next(self, nums: list[int], i: int, direction: bool) -> int:
        is_oob = i == -1
        is_diff_directions = (nums[i] > 0) != direction
        if is_oob or is_diff_directions: return -1

        i_next = (i + nums[i]) % len(nums)
        is_singleton = i_next == i

        return i_next if not is_singleton else -1


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: True)
    nums = [2, -1, 1, 2, 2]
    print(s_init.circularArrayLoop(nums))
    print(s_pref.circularArrayLoop(nums))

    # Example 2 (Expected Output: False)
    nums = [-1, -2, -3, -4, -5, 6]
    print(s_init.circularArrayLoop(nums))
    print(s_pref.circularArrayLoop(nums))

    # Example 3 (Expected Output: True)
    nums = [1, -1, 5, 1, 4]
    print(s_init.circularArrayLoop(nums))
    print(s_pref.circularArrayLoop(nums))

    # Benchmarking
    number = 10_000
    nums = [1, -1, 5, 1, 4]
    print(timeit.timeit(lambda: s_init.circularArrayLoop(nums), number=number))
    print(timeit.timeit(lambda: s_pref.circularArrayLoop(nums), number=number))
