#!/usr/bin/env python3
"""https://leetcode.com/problems/minimum-depth-of-binary-tree/"""

from collections import deque

from tools.dsa.tree import TreeNode


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        depth = 0
        if not root: return depth

        q = deque([root])
        while q:
            depth += 1
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                kid_l, kid_r = node.left, node.right

                is_leaf = not kid_l and not kid_r
                if is_leaf: return depth

                if kid_l: q.append(kid_l)
                if kid_r: q.append(kid_r)
