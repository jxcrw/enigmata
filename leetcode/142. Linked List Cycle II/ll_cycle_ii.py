#!/usr/bin/env python3
"""https://leetcode.com/problems/linked-list-cycle-ii/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        node, seen = head, set()
        while node:
            if node in seen: return node
            seen.add(node)
            node = node.next
        return None


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
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


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: True)
    nums = [3, 2, 0, -4]
    linked_list = LinkedList(nums)
    linked_list.create_cycle(2)
    print(repr((s_init.detectCycle(linked_list.head))))
    print(repr((s_pref.detectCycle(linked_list.head))))

    # Example 2 (Expected Output: True)
    nums = [1, 2]
    linked_list = LinkedList(nums)
    linked_list.create_cycle(1)
    print(repr((s_init.detectCycle(linked_list.head))))
    print(repr((s_pref.detectCycle(linked_list.head))))

    # Example 2 (Expected Output: False)
    nums = [1]
    print(repr((s_init.detectCycle(LinkedList(nums).head))))
    print(repr((s_pref.detectCycle(LinkedList(nums).head))))

    # Benchmarking
    number = 10_000
    nums = list(range(1000))
    linked_list = LinkedList(nums)
    linked_list.create_cycle(500)
    print(repr((s_init.detectCycle(linked_list.head))))
    print(timeit.timeit(lambda: s_init.detectCycle(linked_list.head), number=number))
    print(timeit.timeit(lambda: s_pref.detectCycle(linked_list.head), number=number))
