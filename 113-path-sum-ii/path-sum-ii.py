# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        self.res = []

        def dfs(node, curr_sum, curr_path):
            if not node:
                return

            curr_sum += node.val
            curr_path.append(node.val)

            if not node.left and not node.right and curr_sum == targetSum:
                self.res.append(curr_path.copy())

            dfs(node.left, curr_sum, curr_path)
            dfs(node.right, curr_sum, curr_path)
            curr_path.pop()

            return
        
        dfs(root, 0, [])
        return self.res