#!/usr/bin/env python3
"""https://leetcode.com/problems/path-sum/"""

from tools.dsa.tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, target: int) -> bool:
        has_path = self._dfs(root, target, pathsum=0)
        return has_path

    def _dfs(self, node: TreeNode | None, target: int, pathsum: int) -> bool:
        if not node: return False

        pathsum += node.val
        is_leaf = not node.left and not node.right
        if is_leaf: return pathsum == target

        left = self._dfs(node.left, target, pathsum)
        right = self._dfs(node.right, target, pathsum)
        return left or right


class SolutionAlt:
    def hasPathSum(self, root: TreeNode | None, target: int) -> bool:
        if not root: return False

        pathsum = 0
        stack = [(root, pathsum)]
        while stack:
            node, pathsum = stack.pop()
            kid_l, kid_r = node.left, node.right
            pathsum += node.val

            is_leaf = not kid_l and not kid_r
            if is_leaf and pathsum == target: return True

            if kid_l: stack.append((kid_l, pathsum))
            if kid_r: stack.append((kid_r, pathsum))

        return False
