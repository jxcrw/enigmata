#!/usr/bin/env python3
"""https://leetcode.com/problems/binary-tree-level-order-traversal/"""

from collections import deque

from tools.dsa.tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        levels = []
        if not root: return levels

        q, level = deque([root]), 0
        while q:
            levels.append([])
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                levels[level].append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1

        return levels
