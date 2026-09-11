# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []

        def dfs(node, curr_path):
            if not node:
                return

            if curr_path == "":
                curr_path = str(node.val)
            else:
                curr_path += "->" + str(node.val)
            if not node.left and not node.right:
                self.res.append(curr_path)
                return

            dfs(node.left, curr_path)
            dfs(node.right, curr_path)

        dfs(root, "")
        return self.res
        