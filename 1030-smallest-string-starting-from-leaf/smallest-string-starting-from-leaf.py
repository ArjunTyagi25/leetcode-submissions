# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.min_string = chr(97+26)

        def dfs(node, curr_str):
            if not node:
                return

            curr_str = chr(node.val + 97) + curr_str
            if not node.left and not node.right:
                if curr_str < self.min_string:
                    self.min_string = curr_str
                    return

            dfs(node.left, curr_str)
            dfs(node.right, curr_str)

        dfs(root, "")
        return self.min_string


        