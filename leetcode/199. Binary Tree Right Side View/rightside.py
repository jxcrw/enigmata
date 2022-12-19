#!/usr/bin/env python3
"""https://leetcode.com/problems/binary-tree-right-side-view/"""

from collections import deque
import timeit

from tools.dsa.tree import TreeNode, binary_tree


class Solution:
    # Time / Space: O(n) / O(n)
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        rightmosts = []
        if not root: return rightmosts

        q = deque([root])
        while q:
            n = len(q)
            rightmost = q[0].val
            rightmosts.append(rightmost)
            for i in range(n):
                node = q.popleft()
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return rightmosts


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: [1, 3, 4])
    root = binary_tree([1, 2, 3, None, 5, None, 4])
    print(solution.rightSideView(root))

    # Example 2 (Expected Output: [1, 3])
    root = binary_tree([1, None, 3])
    print(solution.rightSideView(root))

    # Example 3 (Expected Output: [])
    root = binary_tree([])
    print(solution.rightSideView(root))

    # Benchmarking
    number = 1000
    root = binary_tree(list(range(1, 2048)))
    print(timeit.timeit(lambda: solution.rightSideView(root), number=number))
