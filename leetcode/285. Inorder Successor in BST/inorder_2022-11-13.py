#!/usr/bin/env python3
"""https://leetcode.com/problems/inorder-successor-in-bst/"""

from tools.dsa.tree import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        successor, node = None, root
        while node:
            if node.val > p.val:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor


class SolutionAlt:

    prev = None
    successor = None

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        self.prev = self.successor = None
        self._dfs(root, p)
        return self.successor

    def _dfs(self, node: TreeNode | None, p: TreeNode) -> None:
        if not node: return

        self._dfs(node.left, p)

        if self.prev == p and not self.successor:
            self.successor = node
            return
        self.prev = node

        self._dfs(node.right, p)
