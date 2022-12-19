#!/usr/bin/env python3
"""https://leetcode.com/problems/kth-largest-element-in-a-stream/"""

from heapq import heappop, heappush
from random import randint


class KthLargestInit:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        kth_largest = self.kth_largest()
        return kth_largest

    def kth_largest(self) -> int:
        nums, k = self.nums[:], self.k

        def partition(l: int, r: int, p: int) -> int:
            pivot = nums[p]
            nums[p], nums[r] = nums[r], nums[p]

            i_swap = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[i_swap] = nums[i_swap], nums[i]
                    i_swap += 1

            nums[r], nums[i_swap] = nums[i_swap], nums[r]
            return i_swap

        def quickselect(l: int, r: int, k: int) -> int:
            if l == r: return nums[l]

            p = randint(l, r)
            p = partition(l, r, p)

            if k == p:
                return nums[k]
            elif k < p:
                return quickselect(l, p - 1, k)
            else:
                return quickselect(p + 1, r, k)

        n = len(nums)
        kth_largest = quickselect(0, n - 1, n - k)
        return kth_largest


class KthLargestPref:
    # Time / Space: O(n log k) / O(k)
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        h, k = self.heap, self.k
        heappush(h, val)
        if len(h) > k:
            heappop(h)
        return h[0]


if __name__ == '__main__':
    s_init = KthLargestInit(3, [4, 5, 8, 2])
    s_pref = KthLargestPref(3, [4, 5, 8, 2])

    print(s_init.add(3)) # Expected: 4
    print(s_init.add(5)) # Expected: 5
    print(s_init.add(10)) # Expected: 5
    print(s_init.add(9)) # Expected: 8
    print(s_init.add(4), '\n') # Expected: 8

    print(s_pref.add(3)) # Expected: 4
    print(s_pref.add(5)) # Expected: 5
    print(s_pref.add(10)) # Expected: 5
    print(s_pref.add(9)) # Expected: 8
    print(s_pref.add(4)) # Expected: 8
