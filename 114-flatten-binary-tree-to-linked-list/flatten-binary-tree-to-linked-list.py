# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.nodes = []

        def preorder(node):
            if not node:
                return

            self.nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        for i in range(len(self.nodes) - 1):
            currNode = self.nodes[i]
            currNode.left = None
            currNode.right = self.nodes[i+1]
