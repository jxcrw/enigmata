#!/usr/bin/env python3
"""https://leetcode.com/problems/path-sum/"""

from tools.dsa.tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, target: int) -> bool:
        if not root: return False

        is_leaf = not root.left and not root.right
        if is_leaf: return root.val == target

        target -= root.val
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)


class SolutionAlternate:
    def hasPathSum(self, root: TreeNode | None, target: int) -> bool:
        if not root: return False
        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()
            kid_l, kid_r = node.left, node.right

            is_leaf = not kid_l and not kid_r
            if is_leaf and curr_sum == target: return True

            if kid_l: stack.append((kid_l, curr_sum + kid_l.val))
            if kid_r: stack.append((kid_r, curr_sum + kid_r.val))
        return False
