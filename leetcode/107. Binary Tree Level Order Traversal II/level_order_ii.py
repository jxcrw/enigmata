#!/usr/bin/env python3
"""https://leetcode.com/problems/binary-tree-level-order-traversal-ii/"""

from collections import deque
import timeit

from tools.dsa.tree import TreeNode, binary_tree


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
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

        levels.reverse()
        return levels


class SolutionAlternate:
    # Time / Space: O(n) / O(n)
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
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

        levels = levels[::-1]
        return levels


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()

    # Example 1 (Expected Output: [[15, 7], [9, 20], [3]])
    root = binary_tree([3, 9, 20, None, None, 15, 7])
    print(s_init.levelOrderBottom(root))
    print(s_alt.levelOrderBottom(root))

    # Example 2 (Expected Output: [[1]])
    root = binary_tree([1])
    print(s_init.levelOrderBottom(root))
    print(s_alt.levelOrderBottom(root))

    # Example 3 (Expected Output: [])
    root = binary_tree([])
    print(s_init.levelOrderBottom(root))
    print(s_alt.levelOrderBottom(root))

    # Benchmarking
    number = 10_000
    root = binary_tree(list(range(1000)))
    print(timeit.timeit(lambda: s_init.levelOrderBottom(root), number=number))
    print(timeit.timeit(lambda: s_alt.levelOrderBottom(root), number=number))
