#!/usr/bin/env python3
"""https://leetcode.com/problems/linked-list-cycle-ii/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        intersection = self._get_intersection(head)
        if not head or not intersection: return None

        p1, p2 = head, intersection
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def _get_intersection(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return slow
        return None


class SolutionAlternate:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        node, seen = head, set()
        while node:
            if node in seen: return node
            seen.add(node)
            node = node.next
        return None
