#!/usr/bin/env python3
"""https://leetcode.com/problems/diameter-of-binary-tree/"""

from tools.dsa.tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        diameter = 0

        def longest_path(node: TreeNode | None) -> int:
            if not node: return 0

            nonlocal diameter
            left = longest_path(node.left)
            right = longest_path(node.right)
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        longest_path(root)
        return diameter
