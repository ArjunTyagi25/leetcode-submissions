# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        def dfs(node, curr_num):
            if not node:
                return
                
            num = curr_num * 10 + node.val

            if not node.left and not node.right:
                self.nums.append(num)
                return

            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, 0)
        res = 0
        for num in self.nums:
            res += num

        return res
        