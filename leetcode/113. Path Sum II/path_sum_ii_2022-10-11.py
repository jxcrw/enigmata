#!/usr/bin/env python3
"""https://leetcode.com/problems/path-sum-ii/"""

from tools.dsa.tree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, target: int) -> list[list[int]]:
        paths, path = [], []
        self._dfs(root, target, path, paths)
        return paths

    def _dfs(self, node: TreeNode, target: int, path: list[int], paths: list[list[int]]):
        if not node: return
        path.append(node.val)

        is_leaf = not node.left and not node.right
        if is_leaf and node.val == target:
            paths.append(list(path))

        target -= node.val
        self._dfs(node.left, target, path, paths)
        self._dfs(node.right, target, path, paths)

        path.pop()
