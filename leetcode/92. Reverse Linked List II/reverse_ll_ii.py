#!/usr/bin/env python3
"""https://leetcode.com/problems/reverse-linked-list-ii/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class SolutionInitial:
    # Time / Space: O(n) / O(1)
    def reverseBetween(self, head: ListNode | None, m: int, n: int) -> ListNode | None:
        prev, curr = None, head
        for _ in range(m - 1):
            prev = curr
            curr = curr.next
        save, tail = prev, curr

        for _ in range(n - m + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if save: save.next = prev
        else: head = prev
        tail.next = curr

        return head


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def reverseBetween(self, head: ListNode | None, m: int, n: int) -> ListNode | None:
        dummy = save = ListNode(next=head)

        for _ in range(m - 1): save = save.next
        tail = save.next

        for _ in range(n - m):
            temp = save.next
            save.next = tail.next
            tail.next = tail.next.next
            save.next.next = temp

        return dummy.next


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [1, 4, 3, 2, 5])
    nums, m, n = [1, 2, 3, 4, 5], 2, 4
    print(s_init.reverseBetween(LinkedList(nums).head, m, n))
    print(s_pref.reverseBetween(LinkedList(nums).head, m, n))

    # Example 2 (Expected Output: [5])
    nums, m, n = [5], 1, 1
    print(s_init.reverseBetween(LinkedList(nums).head, m, n))
    print(s_pref.reverseBetween(LinkedList(nums).head, m, n))

    # Benchmarking
    number = 10_000
    nums, m, n = list(range(100)), 50, 60
    print(timeit.timeit(lambda: s_init.reverseBetween(LinkedList(nums).head, m, n), number=number))
    print(timeit.timeit(lambda: s_pref.reverseBetween(LinkedList(nums).head, m, n), number=number))
