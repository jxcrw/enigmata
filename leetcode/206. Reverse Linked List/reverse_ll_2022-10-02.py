#!/usr/bin/env python3
"""https://leetcode.com/problems/reverse-linked-list/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


class SolutionAlternate:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        dummy, curr = ListNode(), head
        while curr:
            temp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = temp
        return dummy.next
