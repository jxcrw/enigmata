#!/usr/bin/env python3
"""https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/"""

from collections import deque

from tools.dsa.tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        levels = []
        if not root: return levels

        q, is_even = deque([root]), True
        while q:
            level, n = [], len(q)
            for _ in range(n):
                if is_even:
                    node = q.popleft()
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                else:
                    node = q.pop()
                    if node.right: q.appendleft(node.right)
                    if node.left: q.appendleft(node.left)
                level.append(node.val)
            levels.append(level)
            is_even = not is_even

        return levels
