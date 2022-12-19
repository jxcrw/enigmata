#!/usr/bin/env python3
"""https://leetcode.com/problems/reorder-list/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        middle = self._find_middle(head)
        start_second_half = self._reverse(middle)

        first, second = head, start_second_half
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

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
