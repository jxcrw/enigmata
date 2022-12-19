#!/usr/bin/env python3
"""https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/description/"""

from tools.dsa.tree import TreeNode


class Solution:
    def isValidSequence(self, root: TreeNode | None, nums: list[int]) -> bool:
        is_valid = self._dfs(root, nums, level=0)
        return is_valid

    def _dfs(self, node: TreeNode | None, nums: list[int], level: int) -> bool:
        if not node: return False

        too_deep = level >= len(nums)
        if too_deep: return False

        has_diverged = node.val != nums[level]
        if has_diverged: return False

        is_leaf = not node.left and not node.right
        correct_length = level == len(nums) - 1
        if is_leaf and correct_length: return True

        level += 1
        left = self._dfs(node.left, nums, level)
        right = self._dfs(node.right, nums, level)
        return left or right


class SolutionAlt:
    def isValidSequence(self, root: TreeNode | None, nums: list[int]) -> bool:
        is_valid = self._dfs(root, nums, level=0)
        return is_valid

    def _dfs(self, node: TreeNode | None, nums: list[int], level: int) -> bool:
        done = lambda: not node
        too_deep = lambda: level >= len(nums)
        has_diverged = lambda: node.val != nums[level]
        is_leaf = lambda: not node.left and not node.right
        correct_length = lambda: level == len(nums) - 1

        if done() or too_deep() or has_diverged(): return False
        if is_leaf() and correct_length(): return True

        level += 1
        left = self._dfs(node.left, nums, level)
        right = self._dfs(node.right, nums, level)
        return left or right
