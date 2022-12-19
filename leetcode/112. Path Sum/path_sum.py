#!/usr/bin/env python3
"""https://leetcode.com/problems/path-sum/"""

import timeit

from tools.dsa.tree import TreeNode, binary_tree


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def hasPathSum(self, root: TreeNode | None, target: int) -> bool:
        if not root: return False

        is_leaf = not root.left and not root.right
        if is_leaf: return root.val == target

        target -= root.val
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)


class SolutionAlternate:
    # Time / Space: O(n) / O(n)
    def hasPathSum(self, root: TreeNode | None, target: int) -> bool:
        if not root: return False
        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()
            kid_l, kid_r = node.left, node.right

            is_leaf = not kid_l and not kid_r
            if is_leaf and curr_sum == target: return True

            if kid_l: stack.append((kid_l, curr_sum + kid_l.val))
            if kid_r: stack.append((kid_r, curr_sum + kid_r.val))
        return False


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_alt = SolutionAlternate()

    # Example 1 (Expected Output: True)
    root, target = binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22
    print(s_init.hasPathSum(root, target))
    print(s_alt.hasPathSum(root, target))

    # Example 2 (Expected Output: False)
    root, target = binary_tree([1, 2, 3]), 5
    print(s_init.hasPathSum(root, target))
    print(s_alt.hasPathSum(root, target))

    # Example 3 (Expected Output: False)
    root, target = binary_tree([]), 0
    print(s_init.hasPathSum(root, target))
    print(s_alt.hasPathSum(root, target))

    # Benchmarking
    number = 1000
    root, target = binary_tree(list(range(1000))), 500
    print(timeit.timeit(lambda: s_init.hasPathSum(root, target), number=number))
    print(timeit.timeit(lambda: s_alt.hasPathSum(root, target), number=number))
