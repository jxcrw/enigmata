#!/usr/bin/env python3
"""https://leetcode.com/problems/linked-list-cycle-ii/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        intersection = self._get_intersection(head)
        if not intersection or not head: return None

        p0, p1 = head, intersection
        while p0 != p1:
            p0 = p0.next
            p1 = p1.next
        return p0

    def _get_intersection(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return slow
        return None


class SolutionAlternate:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        seen, node = set(), head
        while node:
            if node in seen: return node
            seen.add(node)
            node = node.next
        return None
