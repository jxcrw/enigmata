#!/usr/bin/env python3
"""https://leetcode.com/problems/diameter-of-binary-tree/"""

import timeit

from tools.dsa.tree import TreeNode, binary_tree


class Solution:
    # Time / Space: O(n) / O(h)
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        diameter = 0

        def longest_path(node: TreeNode | None) -> int:
            if not node: return 0
            nonlocal diameter

            left = longest_path(node.left)
            right = longest_path(node.right)
            diameter = max(diameter, left + right)

            return max(left, right) + 1

        longest_path(root)
        return diameter


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: 3)
    root = binary_tree([1, 2, 3, 4, 5])
    print(solution.diameterOfBinaryTree(root))

    # Example 2 (Expected Output: 1)
    root = binary_tree([1, 2])
    print(solution.diameterOfBinaryTree(root))

    # Benchmarking
    number = 1000
    root = binary_tree(list(range(1000)))
    print(timeit.timeit(lambda: solution.diameterOfBinaryTree(root), number=number))
