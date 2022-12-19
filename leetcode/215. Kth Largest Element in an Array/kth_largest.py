#!/usr/bin/env python3
"""https://leetcode.com/problems/kth-largest-element-in-an-array/"""

from heapq import heappop, heappush, nlargest
import random
import timeit


class SolutionInitial:
    # Time / Space: O(n log n) / O(n)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        kth_largest = nums[-k]
        return kth_largest


class SolutionAlternate:
    # Time / Space: O(n log k) / O(k)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

    def findKthLargest(self, nums: list[int], k: int) -> int:
        kth_largest = nlargest(k, nums)[-1]
        return kth_largest


class SolutionPreferredLite:
    # Time / Space: O(n) / O(n)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.findKthSmallest(nums, len(nums) - k + 1)

    def findKthSmallest(self, nums: list[int], k: int) -> int:
        if not nums: return 0

        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthSmallest(left, k)
        elif k <= L + M:
            return pivot
        else:
            return self.findKthSmallest(right, k - M - L)


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        kth_largest = self.quickselect(nums, 0, n - 1, n - k)
        return kth_largest

    def quickselect(self, nums: list[int], l: int, r: int, k: int) -> int:
        if l == r: return nums[l]

        i_pivot = random.randint(l, r)
        i_pivot = self.partition(nums, l, r, i_pivot)

        if k == i_pivot:
            return nums[k]
        elif k < i_pivot:
            return self.quickselect(nums, l, i_pivot - 1, k)
        else:
            return self.quickselect(nums, i_pivot + 1, r, k)

    def partition(self, nums: list[int], l: int, r: int, i_pivot: int) -> int:
        pivot = nums[i_pivot]
        nums[i_pivot], nums[r] = nums[r], nums[i_pivot]

        i_swap = l
        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[i_swap] = nums[i_swap], nums[i]
                i_swap += 1

        nums[r], nums[i_swap] = nums[i_swap], nums[r]
        return i_swap


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()
    s_pref_lite = SolutionPreferredLite()
    s_pref = SolutionPreferred()

    # Example 0 (Expected Output: 5)
    nums, k = [3, 2, 1, 5, 6, 4], 2
    print(s_init.findKthLargest(list(nums[:]), k))
    print(s_alt.findKthLargest(list(nums[:]), k))
    print(s_pref_lite.findKthLargest(list(nums[:]), k))
    print(s_pref.findKthLargest(list(nums[:]), k))

    # Example 1 (Expected Output: 4)
    nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    print(s_init.findKthLargest(list(nums[:]), k))
    print(s_alt.findKthLargest(list(nums[:]), k))
    print(s_pref_lite.findKthLargest(list(nums[:]), k))
    print(s_pref.findKthLargest(list(nums[:]), k))

    # Benchmarking
    number = 100
    nums, k = list(range(100_000)), 500
    print(timeit.timeit(lambda: s_init.findKthLargest(list(nums[:]), k), number=number))
    print(timeit.timeit(lambda: s_alt.findKthLargest(list(nums[:]), k), number=number))
    print(timeit.timeit(lambda: s_pref_lite.findKthLargest(list(nums[:]), k), number=number))
    print(timeit.timeit(lambda: s_pref.findKthLargest(list(nums[:]), k), number=number))
