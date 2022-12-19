#!/usr/bin/env python3
"""https://leetcode.com/problems/reverse-linked-list/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
