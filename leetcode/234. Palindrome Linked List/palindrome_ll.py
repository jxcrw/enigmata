#!/usr/bin/env python3
"""https://leetcode.com/problems/palindrome-linked-list/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class Solution:
    # Time / Space: O(n) / O(1)
    def isPalindrome(self, head: ListNode | None) -> bool:
        middle = self._find_middle(head)
        start_second_half = self._reverse(middle)

        is_palindrome = True
        p1, p2 = head, start_second_half
        while is_palindrome and p2:
            if p1.val != p2.val:
                is_palindrome = False
            p1 = p1.next
            p2 = p2.next

        middle = self._reverse(start_second_half)
        return is_palindrome

    def _find_middle(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
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


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: True)
    nums = [1, 2, 2, 1]
    print(solution.isPalindrome(LinkedList(nums).head))

    # Example 2 (Expected Output: False)
    nums = [1, 2]
    print(solution.isPalindrome(LinkedList(nums).head))

    # Benchmarking
    number = 10_000
    nums = list(range(100))
    print(timeit.timeit(lambda: solution.isPalindrome(LinkedList(nums).head), number=number))
