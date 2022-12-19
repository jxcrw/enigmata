#!/usr/bin/env python3
"""https://leetcode.com/problems/minimum-depth-of-binary-tree/"""

from collections import deque
import timeit

from tools.dsa.tree import TreeNode, binary_tree


class Solution:
    # Time / Space: O(n) / O(n)
    def minDepth(self, root: TreeNode | None) -> int:
        depth = 0
        if not root: return depth

        q = deque([root])
        while q:
            n = len(q)
            depth += 1
            for _ in range(n):
                node = q.popleft()
                kid_l, kid_r = node.left, node.right

                if not kid_l and not kid_r: return depth
                if kid_l: q.append(kid_l)
                if kid_r: q.append(kid_r)


if __name__ == '__main__':
    s_init = Solution()

    # Example 1 (Expected Output: 2)
    root = binary_tree([3, 9, 20, None, None, 15, 7])
    print(s_init.minDepth(root))

    # Example 2 (Expected Output: 5)
    root = binary_tree([2, None, 3, None, 4, None, 5, None, 6])
    print(s_init.minDepth(root))

    # Benchmarking
    number = 10_000
    root = binary_tree(list(range(1000)))
    print(timeit.timeit(lambda: s_init.minDepth(root), number=number))
