#!/usr/bin/env python3
"""https://leetcode.com/problems/palindrome-linked-list/"""

from tools.dsa.linked_list import ListNode


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        end_first_half = self._find_end_first_half(head)
        start_second_half = self._reverse(end_first_half.next)

        is_palindrome = True
        p0, p1 = head, start_second_half
        while is_palindrome and p1:
            if p0.val != p1.val: is_palindrome = False
            p0 = p0.next
            p1 = p1.next

        end_first_half.next = self._reverse(start_second_half)
        return is_palindrome

    def _find_end_first_half(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _reverse(self, head: ListNode | None) -> ListNode | None:
        node, prev = head, None
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp
        return prev
