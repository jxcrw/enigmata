#!/usr/bin/env python3
"""https://leetcode.com/problems/inorder-successor-in-bst/"""

import timeit

from tools.dsa.tree import TreeNode, binary_tree, get_node


class SolutionInitial:
    # Time / Space: O(n) / O(n)

    prev = None
    successor = None

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        self.prev = self.successor = None
        self._inorder(root, p)
        return self.successor

    def _inorder(self, node: TreeNode, p: TreeNode) ->  TreeNode | None:
        if not node: return

        self._inorder(node.left, p)
        if self.prev == p and not self.successor:
            self.successor = node
            return
        self.prev = node
        self._inorder(node.right, p)


class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        successor, node = None, root
        while node:
            if node.val > p.val:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor


if __name__ == '__main__':
    s_init = SolutionInitial()
    s_pref = SolutionPreferred()

    # Example 1 (Expected Output: 2)
    root = binary_tree([2, 1, 3])
    p = get_node(root, 1)
    print(s_init.inorderSuccessor(root, p))
    print(s_pref.inorderSuccessor(root, p))

    # Example 2 (Expected Output: None)
    root = binary_tree([5, 3, 6, 2, 4, None, None, 1])
    p = get_node(root, 6)
    print(s_init.inorderSuccessor(root, p))
    print(s_pref.inorderSuccessor(root, p))

    # Benchmarking
    number = 1000
    root = binary_tree(list(range(1000)))
    p = get_node(root, 800)
    print(timeit.timeit(lambda: s_init.inorderSuccessor(root, p), number=number))
    print(timeit.timeit(lambda: s_pref.inorderSuccessor(root, p), number=number))
