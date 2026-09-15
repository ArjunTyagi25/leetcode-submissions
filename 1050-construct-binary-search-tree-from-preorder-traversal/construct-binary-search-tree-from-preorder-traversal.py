# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0

        def rec(upper_bound):
            if self.i == len(preorder):
                return None

            if preorder[self.i] < upper_bound:
                node = TreeNode(preorder[self.i])
                self.i += 1
                node.left = rec(node.val)
                node.right = rec(upper_bound)
                return node
            else:
                return None

        return rec(float('inf'))
        