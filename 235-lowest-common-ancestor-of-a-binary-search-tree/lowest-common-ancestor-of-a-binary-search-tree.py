# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        smaller_val = min(p.val, q.val)
        larger_val = max(p.val, q.val)

        def rec(node):
            if not node:
                return None

            if smaller_val <= node.val <= larger_val:
                return node
            elif node.val < smaller_val:
                return rec(node.right)
            elif larger_val < node.val:
                return rec(node.left)

        return rec(root)
        