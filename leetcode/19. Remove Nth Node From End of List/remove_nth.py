#!/usr/bin/env python3
"""https://leetcode.com/problems/remove-nth-node-from-end-of-list/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class Solution:
    # Time / Space: O(n) / O(1)
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = fast = slow = ListNode(next=head)
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: [1, 2, 3, 5])
    nums, n = [1, 2, 3, 4, 5], 2
    print(solution.removeNthFromEnd(LinkedList(nums).head, n))

    # Example 2 (Expected Output: [])
    nums, n = [1], 1
    print(solution.removeNthFromEnd(LinkedList(nums).head, n))

    # Example 3 (Expected Output: [1])
    nums, n = [1, 2], 1
    print(solution.removeNthFromEnd(LinkedList(nums).head, n))

    # Benchmarking
    number = 10_000
    nums, n = list(range(100)), 2
    print(timeit.timeit(lambda: solution.removeNthFromEnd(LinkedList(nums).head, n), number=number))
