#!/usr/bin/env python3
"""https://leetcode.com/problems/path-sum-iii/"""

from collections import defaultdict

from tools.dsa.tree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, target: int) -> int:
        count_sums = defaultdict(int, {0: 1})

        def _dfs(node: TreeNode | None, prefix_sum: int) -> int:
            if not node: return 0

            prefix_sum += node.val
            diff = prefix_sum - target
            count = count_sums.get(diff, 0)

            count_sums[prefix_sum] += 1
            count += _dfs(node.left, prefix_sum)
            count += _dfs(node.right, prefix_sum)

            count_sums[prefix_sum] -= 1
            return count

        count = _dfs(root, prefix_sum=0)
        return count
