# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.strings = [] 
        def dfs(node, curr_str):
            if not node:
                return

            curr_str += chr(node.val + 97)
            if not node.left and not node.right:
                self.strings.append(curr_str[::-1])
                curr_str = curr_str[:-1]
                return

            dfs(node.left, curr_str)
            dfs(node.right, curr_str)
            curr_str = curr_str[:-1]
            return

        dfs(root, "")
        return sorted(self.strings)[0]


        