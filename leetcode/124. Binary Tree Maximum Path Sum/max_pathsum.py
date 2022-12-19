#!/usr/bin/env python3
"""https://leetcode.com/problems/binary-tree-maximum-path-sum/"""

import timeit

from tools.dsa.tree import TreeNode, binary_tree


class Solution:
    # Time / Space: O(n) / O(h)
    def maxPathSum(self, root: TreeNode | None) -> float:
        max_sum = -float('inf')

        def max_gain(node: TreeNode | None) -> int:
            if not node: return 0
            nonlocal max_sum

            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)
            max_sum = max(max_sum, node.val + left + right)

            return node.val + max(left, right)

        max_gain(root)
        return max_sum


if __name__ == '__main__':
    solution = Solution()

    # Example 0 (Expected Output: 6)
    root = binary_tree([1,  2,  3])
    print(solution.maxPathSum(root))

    # Example 1 (Expected Output: 42)
    root = binary_tree([-10,  9,  20,  None,  None,  15,  7])
    print(solution.maxPathSum(root))

    # Benchmarking
    number = 10_000
    root = binary_tree([-10,  9,  20,  None,  None,  15,  7])
    print(timeit.timeit(lambda: solution.maxPathSum(root), number=number))
