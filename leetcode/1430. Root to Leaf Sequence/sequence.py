#!/usr/bin/env python3
"""https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/description/"""

import random

from tools.dsa.tree import TreeNode, binary_tree
from tools.lc_tools import benchmark, pretty_eval


class SolutionInit:
    # Time / Space: O(n) / O(h)
    def isValidSequence(self, root: TreeNode | None, nums: list[int]) -> bool:
        path, target = '', ''.join(map(str, nums))
        is_sequence = self._dfs(root, path, target)
        return is_sequence

    def _dfs(self, node: TreeNode | None, path: str, target: str) -> bool:
        if not node: return False
        path += str(node.val)

        is_leaf = not node.left and not node.right
        if is_leaf: return path == target

        return self._dfs(node.left, path, target) or self._dfs(node.right, path, target)


class SolutionAlt:
    # Time / Space: O(n) / O(h)
    def isValidSequence(self, root: TreeNode | None, nums: list[int]) -> bool:
        if not root: return False
        level = 0
        stack = [(root, level)]
        while stack:
            node, level = stack.pop()

            too_deep = level >= len(nums)
            if too_deep: continue

            has_diverged = node.val != nums[level]
            if has_diverged: continue

            is_leaf = not node.left and not node.right
            correct_length = level == len(nums) - 1
            if is_leaf and correct_length: return True

            if node.left: stack.append((node.left, level + 1))
            if node.right: stack.append((node.right, level + 1))
        return False


class SolutionPref:
    # Time / Space: O(n) / O(h)
    def isValidSequence(self, root: TreeNode | None, nums: list[int]) -> bool:
        is_sequence = self._dfs(root, nums, level=0)
        return is_sequence

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


class SolutionPrefAlt:
    # Time / Space: O(n) / O(h)
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


if __name__ == '__main__':
    # Setup
    s_init = SolutionInit()
    s_alt = SolutionAlt()
    s_pref = SolutionPref()
    s_pref_alt = SolutionPrefAlt()
    solutions = [s_init, s_alt, s_pref, s_pref_alt]
    method = 'isValidSequence'

    # Examples
    inputs = [(binary_tree([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]), [0, 1, 0, 1]),
              (binary_tree([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]), [0, 0, 1]),
              (binary_tree([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]), [0, 1, 1])]
    outputs = [True, False, False]
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 1000
    root, path = binary_tree(list(range(1024))), list(range(100))
    random.shuffle(path)
    args = (root, path)
    benchmark(solutions, method, args, number)
