# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        def post_order(node):
            if not node:
                return (0, 0) # Sum of subtree, number of nodes

            left_subtree = post_order(node.left)
            right_subtree = post_order(node.right)
            s = (node.val + left_subtree[0] + right_subtree[0])
            count = 1 + left_subtree[1] + right_subtree[1]

            if s//count == node.val:
                self.res += 1

            return (s, count)

        post_order(root)
        return self.res
        