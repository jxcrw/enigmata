#!/usr/bin/env python3
"""https://leetcode.com/problems/binary-tree-right-side-view/"""

from collections import deque

from tools.dsa.tree import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        rightmosts = []
        if not root: return rightmosts

        q = deque([root])
        while q:
            rightmost = q[0].val
            rightmosts.append(rightmost)
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)

        return rightmosts
