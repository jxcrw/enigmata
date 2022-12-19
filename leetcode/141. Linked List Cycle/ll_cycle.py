#!/usr/bin/env python3
"""https://leetcode.com/problems/linked-list-cycle/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def hasCycle(self, head: ListNode | None) -> bool:
        node, seen = head, set()
        while node:
            if node in seen: return True
            seen.add(node)
            node = node.next
        return False

class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: True)
    nums = [3, 2, 0, -4]
    linked_list = LinkedList(nums)
    linked_list.create_cycle(2)
    print(s_init.hasCycle(linked_list.head))
    print(s_pref.hasCycle(linked_list.head))

    # Example 2 (Expected Output: True)
    nums = [1, 2]
    linked_list = LinkedList(nums)
    linked_list.create_cycle(1)
    print(s_init.hasCycle(linked_list.head))
    print(s_pref.hasCycle(linked_list.head))

    # Example 2 (Expected Output: False)
    nums = [1]
    print(s_init.hasCycle(LinkedList(nums).head))
    print(s_pref.hasCycle(LinkedList(nums).head))

    # Benchmarking
    number = 10_000
    nums = list(range(1000))
    linked_list = LinkedList(nums)
    linked_list.create_cycle(500)
    print(timeit.timeit(lambda: s_init.hasCycle(linked_list.head), number=number))
    print(timeit.timeit(lambda: s_pref.hasCycle(linked_list.head), number=number))
