# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def checkSymmetric(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            if node1 and not node2:
                return False
            if node1 and node2:
                return node1.val == node2.val and checkSymmetric(node1.left, node2.right) and checkSymmetric(node1.right, node2.left)

        return checkSymmetric(root, root)

