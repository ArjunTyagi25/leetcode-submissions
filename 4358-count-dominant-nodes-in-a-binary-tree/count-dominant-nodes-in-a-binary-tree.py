# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.res = 0
        def postorder(node):
            if not node:
                return float('-inf')

            leftSubtreeVal = postorder(node.left)
            rightSubtreeVal = postorder(node.right)
            if node.val >= max(leftSubtreeVal, rightSubtreeVal):
                self.res += 1
            
            return max(node.val, leftSubtreeVal, rightSubtreeVal)

        postorder(root)
        return self.res