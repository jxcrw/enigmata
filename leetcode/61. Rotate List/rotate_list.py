#!/usr/bin/env python3
"""https://leetcode.com/problems/rotate-list/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class Solution:
    # Time / Space: O(n) / O(1)
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next: return head

        n, tail = 1, head
        while tail.next:
            n += 1
            tail = tail.next

        k %= n
        if k == 0: return head
        tail.next = head

        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: [4, 5, 1, 2, 3])
    nums, k = [1, 2, 3, 4, 5], 2
    print(solution.rotateRight(LinkedList(nums).head, k))

    # Example 2 (Expected Output: [2, 0, 1])
    nums, k = [0, 1, 2], 4
    print(solution.rotateRight(LinkedList(nums).head, k))

    # Benchmarking
    number = 1000
    nums, k = list(range(1000)), 499
    print(timeit.timeit(lambda: solution.rotateRight(LinkedList(nums).head, k), number=number))
