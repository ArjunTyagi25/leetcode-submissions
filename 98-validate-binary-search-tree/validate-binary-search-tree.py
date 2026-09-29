# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def checkRootRange(node, leftBound, rightBound):
            if not node:
                return True

            if leftBound < node.val < rightBound:
                return checkRootRange(node.left, leftBound, node.val) and checkRootRange(node.right, node.val, rightBound)
            else:
                return False

        return checkRootRange(root, float('-inf'), float('inf'))