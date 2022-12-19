#!/usr/bin/env python3
"""https://leetcode.com/problems/rotate-list/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next: return head

        n, tail = 1, head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0: return head
        tail.next = head

        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
