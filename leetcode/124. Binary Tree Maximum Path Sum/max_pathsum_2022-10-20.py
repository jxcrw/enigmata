#!/usr/bin/env python3
"""https://leetcode.com/problems/binary-tree-maximum-path-sum/"""

from tools.dsa.tree import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> float:
        max_sum = -float('inf')

        def max_gain(node: TreeNode | None) -> int:
            if not node: return 0
            nonlocal max_sum

            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)
            max_sum = max(max_sum, node.val + left + right)

            return node.val + max(left, right)

        max_gain(root)
        return max_sum
