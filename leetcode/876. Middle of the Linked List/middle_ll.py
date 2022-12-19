#!/usr/bin/env python3
"""https://leetcode.com/problems/middle-of-the-linked-list/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class SolutionInitial:
    # Time / Space: O(n) / O(1)
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        n, node = 0, head
        while node:
            node = node.next
            n += 1

        n_mid, mid = n // 2, head
        for _ in range(n_mid): mid = mid.next

        return mid


class SolutionAlternate:
    # Time / Space: O(n) / O(n)
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        n, node, nodes = 0, head, {}
        while node:
            n += 1
            nodes[n] = node
            node = node.next

        n_mid = n // 2 + 1
        mid = nodes[n_mid]
        return mid


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [3, 4, 5])
    nums = [1, 2, 3, 4, 5]
    print(s_init.middleNode(LinkedList(nums).head))
    print(s_pref.middleNode(LinkedList(nums).head))

    # Example 2 (Expected Output: [4, 5, 6])
    nums = [1, 2, 3, 4, 5, 6]
    print(s_init.middleNode(LinkedList(nums).head))
    print(s_pref.middleNode(LinkedList(nums).head))

    # Benchmarking
    number = 10_000
    nums = list(range(100))
    print(timeit.timeit(lambda: s_init.middleNode(LinkedList(nums).head), number=number))
    print(timeit.timeit(lambda: s_pref.middleNode(LinkedList(nums).head), number=number))
