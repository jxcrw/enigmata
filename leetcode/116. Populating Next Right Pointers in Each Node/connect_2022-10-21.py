#!/usr/bin/env python3
"""https://leetcode.com/problems/populating-next-right-pointers-in-each-node/"""

from collections import deque

from tools.dsa.tree import TreeNode


class Solution:
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


class SolutionAlternate:
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
