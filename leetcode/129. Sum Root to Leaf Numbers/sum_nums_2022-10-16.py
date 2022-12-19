#!/usr/bin/env python3
"""https://leetcode.com/problems/sum-root-to-leaf-numbers/"""

from tools.dsa.tree import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        total = self._dfs(root, path=0)
        return total

    def _dfs(self, node: TreeNode | None, path: int) -> int:
        if not node: return 0
        path = path * 10 + node.val

        is_leaf = not node.left and not node.right
        if is_leaf: return path

        left = self._dfs(node.left, path)
        right = self._dfs(node.right, path)
        return left + right


class SolutionAlternate:
    def sumNumbers(self, root: TreeNode | None) -> int:
        total = path = 0
        if not root: return total

        stack = [(root, path)]
        while stack:
            node, path = stack.pop()
            kid_l, kid_r = node.left, node.right
            path = path * 10 + node.val

            is_leaf = not kid_l and not kid_r
            if is_leaf: total += path

            if kid_l: stack.append((kid_l, path))
            if kid_r: stack.append((kid_r, path))

        return total
