# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i+1].val:
                j = i + 1
                while j != len(nodes) and nodes[j].val < nodes[i].val:
                    j += 1
                nodes[i].val, nodes[j-1].val = nodes[j-1].val, nodes[i].val
                

        