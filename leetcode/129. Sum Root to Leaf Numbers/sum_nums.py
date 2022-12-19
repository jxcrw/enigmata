#!/usr/bin/env python3
"""https://leetcode.com/problems/sum-root-to-leaf-numbers/"""

import timeit

from tools.dsa.tree import TreeNode, binary_tree


class SolutionInitial:
    # Time / Space: O(n) / O(h)

    total = 0

    def sumNumbers(self, root: TreeNode | None) -> int:
        self.total = path = 0
        self._dfs(root, path)
        return self.total

    def _dfs(self, node: TreeNode | None, path: int):
        if not node: return
        path = path * 10 + node.val

        is_leaf = not node.left and not node.right
        if is_leaf:
            self.total += path
        else:
            self._dfs(node.left, path)
            self._dfs(node.right, path)


class SolutionAlternate:
    # Time / Space: O(n) / O(h)
    def sumNumbers(self, root: TreeNode | None) -> int:
        path = 0
        total = self._dfs(root, path)
        return total

    def _dfs(self, node: TreeNode | None, path: int) -> int:
        if not node: return 0
        path = path * 10 + node.val

        is_leaf = not node.left and not node.right
        if is_leaf: return path

        return self._dfs(node.left, path) + self._dfs(node.right, path)


class SolutionPreferred:
    # Time / Space: O(n) / O(h)
    def sumNumbers(self, root: TreeNode | None) -> int:
        total = path = 0
        if not root: return total

        stack = [(root, path)]
        while stack:
            node, path = stack.pop()
            kid_l, kid_r = node.left, node.right
            path = path * 10 + node.val

            is_leaf = not kid_l and not kid_r
            if is_leaf: total += path

            if kid_l: stack.append((kid_l, path))
            if kid_r: stack.append((kid_r, path))

        return total


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 25)
    root = binary_tree([1, 2, 3])
    print(s_init.sumNumbers(root))
    print(s_alt.sumNumbers(root))
    print(s_pref.sumNumbers(root))

    # Example 2 (Expected Output: 1026)
    root = binary_tree([4, 9, 0, 5, 1])
    print(s_init.sumNumbers(root))
    print(s_alt.sumNumbers(root))
    print(s_pref.sumNumbers(root))

    # Benchmarking
    number = 10_000
    root = binary_tree([4, 9, 0, 5, 1])
    print(timeit.timeit(lambda: s_init.sumNumbers(root), number=number))
    print(timeit.timeit(lambda: s_alt.sumNumbers(root), number=number))
    print(timeit.timeit(lambda: s_pref.sumNumbers(root), number=number))
