#!/usr/bin/env python3
"""https://leetcode.com/problems/remove-nth-node-from-end-of-list/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = fast = slow = ListNode(next=head)
        for _ in range(n): fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
