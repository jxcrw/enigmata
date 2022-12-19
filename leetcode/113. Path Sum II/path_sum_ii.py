#!/usr/bin/env python3
"""https://leetcode.com/problems/path-sum-ii/"""

import timeit

from tools.dsa.tree import TreeNode, binary_tree


class Solution:
    # Time / Space: O(n^2) / O(n)
    def pathSum(self, root: TreeNode | None, target: int) -> list[list[int]]:
        paths, path = [], []
        self._dfs(root, target, path, paths)
        return paths

    def _dfs(self, node: TreeNode | None, target: int, path: list[int], paths: list[list[int]]):
        if not node: return
        path.append(node.val)

        is_leaf = not node.left and not node.right
        if is_leaf and node.val == target:
            paths.append(path[:])
        else:
            target -= node.val
            self._dfs(node.left, target, path, paths)
            self._dfs(node.right, target, path, paths)

        path.pop()


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: [[5, 4, 11, 2], [5, 8, 4, 5]])
    root, target = binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22
    print(solution.pathSum(root, target))

    # Example 2 (Expected Output: [])
    root, target = binary_tree([1, 2, 3]), 5
    print(solution.pathSum(root, target))

    # Example 3 (Expected Output: [])
    root, target = binary_tree([1, 2]), 0
    print(solution.pathSum(root, target))

    # Benchmarking
    number = 1000
    root, target = binary_tree(list(range(1000))), 500
    print(timeit.timeit(lambda: solution.pathSum(root, target), number=number))
