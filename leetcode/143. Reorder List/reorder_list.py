#!/usr/bin/env python3
"""https://leetcode.com/problems/reorder-list/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class Solution:
    # Time / Space: O(n) / O(1)
    def reorderList(self, head: ListNode | None) -> None:
        middle = self._find_middle(head)
        start_second_half = self._reverse(middle)

        first, second = head, start_second_half
        while second.next:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp
        return head

    def _find_middle(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _reverse(self, head: ListNode | None) -> ListNode | None:
        node, prev = head, None
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp
        return prev


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: [1, 4, 2, 3])
    nums = [1, 2, 3, 4]
    print(solution.reorderList(LinkedList(nums).head))

    # Example 2 (Expected Output: [1, 5, 2, 4, 3])
    nums = [1, 2, 3, 4, 5]
    print(solution.reorderList(LinkedList(nums).head))

    # Benchmarking
    number = 10_000
    nums = list(range(100))
    print(timeit.timeit(lambda: solution.reorderList(LinkedList(nums).head), number=number))
