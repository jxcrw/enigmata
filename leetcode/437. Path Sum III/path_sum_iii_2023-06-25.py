#!/usr/bin/env python3
"""https://leetcode.com/problems/path-sum-iii/"""

from collections import defaultdict

from tools.dsa.tree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, target: int) -> int:
        sum_counts = defaultdict(int, {0: 1})

        def dfs(node: TreeNode | None, prefix_sum: int) -> int:
            if not node: return 0

            prefix_sum += node.val
            diff = prefix_sum - target
            count = sum_counts.get(diff, 0)

            sum_counts[prefix_sum] += 1
            count += dfs(node.left, prefix_sum)
            count += dfs(node.right, prefix_sum)

            sum_counts[prefix_sum] -= 1
            return count

        total = dfs(root, prefix_sum=0)
        return total
