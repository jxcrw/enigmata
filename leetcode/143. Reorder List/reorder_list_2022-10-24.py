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

    def _reverse(self, node: ListNode | None) -> ListNode | None:
        curr, prev = node, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
