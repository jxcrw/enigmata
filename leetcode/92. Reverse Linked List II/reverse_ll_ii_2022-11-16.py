#!/usr/bin/env python3
"""https://leetcode.com/problems/reverse-linked-list-ii/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def reverseBetween(self, head: ListNode | None, m: int, n: int) -> ListNode | None:
        dummy = save = ListNode(next=head)

        for _ in range(m - 1): save = save.next
        tail = save.next

        for _ in range(n - m):
            temp = save.next
            save.next = tail.next
            tail.next = tail.next.next
            save.next.next = temp

        return dummy.next
