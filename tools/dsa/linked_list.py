#!/usr/bin/env python3
"""Linked list stuff"""

from typing import Any


class LinkedList:
    """A simple singly-linked list with some debugging features."""
    def __init__(self, vals: list[Any]):
        self.head = None
        self.nodes = []

        for i, val in enumerate(vals):
            node = ListNode(val)
            self.nodes.append(node)
            if i == 0:
                self.head = node
            else:
                self.nodes[i - 1].next = node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        return str([node.val for node in self])

    def create_cycle(self, n):
        """Intentionally create a cycle from the tail to the nth node."""
        self.nodes[-1].next = self.nodes[n - 1]


class ListNode:
    """A node in a linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'

    def __str__(self):
        return f'{self.val} > {self.next}'


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)

    head = a
    a.next = b
    b.next = c
    c.next = d
    d.next = None

    my_list = LinkedList([1, 2, 3, 4])
    my_list2 = LinkedList([1])
    my_list3 = LinkedList([])
