#!/usr/bin/env python3
"""https://leetcode.com/problems/middle-of-the-linked-list/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
