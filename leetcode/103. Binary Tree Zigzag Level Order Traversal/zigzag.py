#!/usr/bin/env python3
"""https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/"""

from collections import deque
import timeit

from tools.dsa.tree import TreeNode, binary_tree


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
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

            if level % 2: levels[level].reverse()
            level += 1

        return levels


class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        levels = []
        if not root: return levels

        q, even_level = deque([root]), True
        while q:
            level, n = [], len(q)
            for _ in range(n):
                if even_level:
                    node = q.popleft()
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                else:
                    node = q.pop()
                    if node.right: q.appendleft(node.right)
                    if node.left: q.appendleft(node.left)
                level.append(node.val)
            levels.append(level)
            even_level = not even_level

        return levels


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: [[3], [20, 9], [15, 7]])
    root = binary_tree([3, 9, 20, None, None, 15, 7])
    print(s_init.zigzagLevelOrder(root))
    print(s_pref.zigzagLevelOrder(root))

    # Example 2 (Expected Output: [[1]])
    root = binary_tree([1])
    print(s_init.zigzagLevelOrder(root))
    print(s_pref.zigzagLevelOrder(root))

    # Example 3 (Expected Output: [])
    root = binary_tree([])
    print(s_init.zigzagLevelOrder(root))
    print(s_pref.zigzagLevelOrder(root))

    # Benchmarking
    number = 10_000
    root = binary_tree(list(range(1000)))
    print(timeit.timeit(lambda: s_init.zigzagLevelOrder(root), number=number))
    print(timeit.timeit(lambda: s_pref.zigzagLevelOrder(root), number=number))
