#!/usr/bin/env python3
"""https://leetcode.com/problems/reverse-nodes-in-k-group/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next

        dummy = nhead = ListNode()
        curr = head
        for _ in range(n // k):
            ntail = curr
            for _ in range(k):
                temp = curr.next
                curr.next = nhead.next
                nhead.next = curr
                curr = temp
            nhead = ntail
        ntail.next = curr

        return dummy.next
