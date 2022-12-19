#!/usr/bin/env python3
"""https://leetcode.com/problems/linked-list-cycle/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False


class SolutionAlternate:
    def hasCycle(self, head: ListNode | None) -> bool:
        node, seen = head, set()
        while node:
            if node in seen: return True
            seen.add(node)
            node = node.next
        return False
