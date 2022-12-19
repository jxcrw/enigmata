#!/usr/bin/env python3
"""https://leetcode.com/problems/path-sum-iii/"""

from collections import defaultdict
import timeit

from tools.dsa.tree import TreeNode, binary_tree


class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def pathSum(self, root: TreeNode | None, target: int) -> int:
        count = 0
        sum_counts = defaultdict(int, {0: 1})

        def _dfs(node: TreeNode | None, prefix_sum: int) -> None:
            if not node: return
            nonlocal count

            prefix_sum += node.val

            diff = prefix_sum - target
            count += sum_counts.get(diff, 0)

            sum_counts[prefix_sum] += 1
            _dfs(node.left, prefix_sum)
            _dfs(node.right, prefix_sum)
            sum_counts[prefix_sum] -= 1

        _dfs(root, prefix_sum=0)
        return count


class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def pathSum(self, root: TreeNode | None, target: int) -> int:
        sum_counts = defaultdict(int, {0: 1})

        def _dfs(node: TreeNode | None, prefix_sum: int) -> int:
            if not node: return 0

            prefix_sum += node.val
            diff = prefix_sum - target
            count = sum_counts.get(diff, 0)

            sum_counts[prefix_sum] += 1
            count += _dfs(node.left, prefix_sum)
            count += _dfs(node.right, prefix_sum)

            sum_counts[prefix_sum] -= 1
            return count

        count = _dfs(root, prefix_sum=0)
        return count


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 3)
    root, target = binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8
    print(s_init.pathSum(root,target))
    print(s_pref.pathSum(root,target))

    # Example 2 (Expected Output: 3)
    root, target = binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22
    print(s_init.pathSum(root,target))
    print(s_pref.pathSum(root,target))

    # Benchmarking
    number = 10_000
    root, target = binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22
    print(timeit.timeit(lambda: s_init.pathSum(root,target), number=number))
    print(timeit.timeit(lambda: s_pref.pathSum(root,target), number=number))
