#!/usr/bin/env python3
"""https://leetcode.com/problems/reverse-nodes-in-k-group/"""

import timeit

from tools.dsa.linked_list import LinkedList, ListNode


class SolutionInitial:
    # Time / Space: O(n^2ish) / O(1)
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next

        m, n = 1, k
        for _ in range(length // k):
            head = self.reverseBetween(head, m, n)
            m += k
            n += k
        return head

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


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next

        dummy = nhead = ListNode()
        curr = head
        for _ in range(n // k):
            ntail = curr
            for _ in range(k):
                temp = curr.next
                curr.next = nhead.next
                nhead.next = curr
                curr = temp
            nhead = ntail
        ntail.next = curr

        return dummy.next


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [2, 1, 4, 3, 5])
    nums, k = [1, 2, 3, 4, 5], 2
    print(s_init.reverseKGroup(LinkedList(nums).head, k))
    print(s_pref.reverseKGroup(LinkedList(nums).head, k))

    # Example 2 (Expected Output: [3, 2, 1, 4, 5])
    nums, k = [1, 2, 3, 4, 5], 3
    print(s_init.reverseKGroup(LinkedList(nums).head, k))
    print(s_pref.reverseKGroup(LinkedList(nums).head, k))

    # Benchmarking
    number = 100
    nums, k = list(range(1000)), 2
    print(timeit.timeit(lambda: s_init.reverseKGroup(LinkedList(nums).head, k), number=number))
    print(timeit.timeit(lambda: s_pref.reverseKGroup(LinkedList(nums).head, k), number=number))
