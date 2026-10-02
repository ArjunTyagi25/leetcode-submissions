# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None

        preorder = deque(preorder)
        inorderIndex = {inorder[i] : i for i in range(len(inorder))}

        def dfs(L, R):
            if L > R:
                return None

            if preorder:
                node = TreeNode(preorder.popleft())
                index = inorderIndex[node.val]
                node.left = dfs(L, index-1)
                node.right = dfs(index+1, R)
                return node

        return dfs(0, len(inorder)-1)