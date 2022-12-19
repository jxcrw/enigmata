#!/usr/bin/env python3
"""https://leetcode.com/problems/reverse-linked-list/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class SolutionIterative:
    # Time / Space: O(n) / O(1)
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


class SolutionIterativeAlt:
    # Time / Space: O(n) / O(1)
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr, dummy = head, ListNode()
        while curr:
            temp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = temp
        return dummy.next


class SolutionRecursive:
    # Time / Space: O(n) / O(n)
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node


if __name__ == '__main__':
    s_iterative = SolutionIterative()
    s_iterative_alt = SolutionIterativeAlt()
    s_recursive = SolutionRecursive()

    # Example 1 (Expected Output: [5, 4, 3, 2, 1])
    nums = [1, 2, 3, 4, 5]
    print(s_iterative.reverseList(LinkedList(nums).head))
    print(s_iterative_alt.reverseList(LinkedList(nums).head))
    print(s_recursive.reverseList(LinkedList(nums).head))

    # Example 2 (Expected Output: [2, 1])
    nums = [1, 2]
    print(s_iterative.reverseList(LinkedList(nums).head))
    print(s_iterative_alt.reverseList(LinkedList(nums).head))
    print(s_recursive.reverseList(LinkedList(nums).head))

    # Example 3 (Expected Output: [])
    nums = []
    print(s_iterative.reverseList(LinkedList(nums).head))
    print(s_iterative_alt.reverseList(LinkedList(nums).head))
    print(s_recursive.reverseList(LinkedList(nums).head))

    # Benchmarking
    number = 10_000
    nums = list(range(100))
    print(timeit.timeit(lambda: s_iterative.reverseList(LinkedList(nums).head), number=number))
    print(timeit.timeit(lambda: s_iterative_alt.reverseList(LinkedList(nums).head), number=number))
    print(timeit.timeit(lambda: s_recursive.reverseList(LinkedList(nums).head), number=number))
