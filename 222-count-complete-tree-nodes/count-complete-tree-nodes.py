# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        def getHeight(node, direction):
            if not node:
                return 0

            if direction == "left":
                return 1 + getHeight(node.left, direction)
            if direction == "right":
                return 1 + getHeight(node.right, direction)

        def rec(node):
            if not node:
                return 0

            leftHeight = getHeight(node, "left")
            rightHeight = getHeight(node, "right")

            if leftHeight == rightHeight:
                return pow(2, leftHeight) - 1
            else:
                return 1 + rec(node.left) + rec(node.right)

        return rec(root)