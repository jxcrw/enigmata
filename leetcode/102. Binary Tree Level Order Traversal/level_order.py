#!/usr/bin/env python3
"""https://leetcode.com/problems/binary-tree-level-order-traversal/"""

from collections import deque
import timeit

from tools.dsa.tree import TreeNode, binary_tree


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        levels = []
        if not root: return levels
        self._dfs(root, 0, levels)
        return levels

    def _dfs(self, node: TreeNode | None, level: int, levels: list[list[int]]):
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)

        if node.left:
            self._dfs(node.left, level + 1, levels)
        if node.right:
            self._dfs(node.right, level + 1, levels)

class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        levels = []
        if not root: return levels

        q, level = deque([root]), 0
        while q:
            levels.append([])
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                levels[level].append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1

        return levels


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [[3], [9, 20], [15, 7]])
    root = binary_tree([3, 9, 20, None, None, 15, 7])
    print(s_init.levelOrder(root))
    print(s_pref.levelOrder(root))

    # Example 2 (Expected Output: [[1]])
    root = binary_tree([1])
    print(s_init.levelOrder(root))
    print(s_pref.levelOrder(root))

    # Example 3 (Expected Output: [])
    root = binary_tree([])
    print(s_init.levelOrder(root))
    print(s_pref.levelOrder(root))

    # Benchmarking
    number = 10_000
    root = binary_tree(list(range(1000)))
    print(timeit.timeit(lambda: s_init.levelOrder(root), number=number))
    print(timeit.timeit(lambda: s_pref.levelOrder(root), number=number))
