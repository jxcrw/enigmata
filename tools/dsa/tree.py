#!/usr/bin/env python3
"""Tree and binary tree stuff"""

from collections import deque
from typing import Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'<{self.val} | {self.left} | {self.right}>'

    def __str__(self) -> str:
        return str(self.val)


def binary_tree(items: list[Any]) -> TreeNode | None:
    """Create a binary tree from a list of items."""
    if not items: return None
    it = iter(items)

    root = TreeNode(next(it))
    q = deque([root])
    while q:
        node = q.popleft()
        left, right = next(it, None), next(it, None)

        if left is not None:
            node.left = TreeNode(left)
            q.append(node.left)
        if right is not None:
            node.right = TreeNode(right)
            q.append(node.right)
    return root


def get_node(root: TreeNode, val: Any) -> TreeNode | None:
    """Get some node of interest from a binary tree."""
    q = deque([root])
    while q:
        node = q.popleft()
        if node.val == val: return node
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return None
