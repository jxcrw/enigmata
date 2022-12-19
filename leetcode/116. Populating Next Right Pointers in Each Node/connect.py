#!/usr/bin/env python3
"""https://leetcode.com/problems/populating-next-right-pointers-in-each-node/"""

from collections import deque
import timeit

from tools.dsa.tree import TreeNode, binary_tree


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def connect(self, root: TreeNode | None) -> TreeNode | None:
        if not root: return root
        q = deque([root])

        while q:
            prev, n = None, len(q)
            for _ in range(n):
                node = q.popleft()
                node.next, prev = prev, node
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)

        return root


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def connect(self, root: TreeNode | None) -> TreeNode | None:
        if not root: return root

        leftmost = root
        while leftmost.left:
            curr = leftmost
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            leftmost = leftmost.left

        return root


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [1, #, 2, 3, #, 4, 5, 6, 7, #])
    root = binary_tree([1, 2, 3, 4, 5, 6, 7])
    print(s_init.connect(root))
    print(s_pref.connect(root))

    # Example 2 (Expected Output: [])
    root = binary_tree([])
    print(s_init.connect(root))
    print(s_pref.connect(root))

    # Benchmarking
    number = 1000
    root = binary_tree(list(range(1, 2048)))
    print(timeit.timeit(lambda: s_init.connect(root), number=number))
    print(timeit.timeit(lambda: s_pref.connect(root), number=number))
