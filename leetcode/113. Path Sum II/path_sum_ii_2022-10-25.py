#!/usr/bin/env python3
"""https://leetcode.com/problems/path-sum-ii/"""

from tools.dsa.tree import TreeNode, binary_tree


class Solution:
    def pathSum(self, root: TreeNode | None, target: int) -> list[list[int]]:
        paths = []

        def dfs(node: TreeNode | None, path: list[int]) -> None:
            if not node: return
            nonlocal target
            path.append(node.val)

            is_leaf = not node.left and not node.right
            matched_target = node.val == target
            if is_leaf and matched_target: paths.append(list(path))

            target -= node.val
            dfs(node.left, path)
            dfs(node.right, path)

            target += node.val
            path.pop()

        dfs(root, path=[])
        return paths


class SolutionPreferred:
    def pathSum(self, root: TreeNode | None, target: int) -> list[list[int]]:
        paths, path = [], []
        self._dfs(root, target, paths, path)
        return paths

    def _dfs(self, node: TreeNode | None, target: int, paths: list[list[int]], path: list[int]):
        if not node: return
        path.append(node.val)

        is_leaf = not node.left and not node.right
        if is_leaf and node.val == target:
            paths.append(list(path))

        target -= node.val
        self._dfs(node.left, target, paths, path)
        self._dfs(node.right, target, paths, path)

        path.pop()
