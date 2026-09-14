# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def postorder(node):
            if not node:
                return (0, 0)

            left_node_robbed, left_node_not_robbed = postorder(node.left)
            right_node_robbed, right_node_not_robbed = postorder(node.right)

            node_robbed = node.val + left_node_not_robbed + right_node_not_robbed
            node_not_robbed = max(left_node_robbed, left_node_not_robbed) + max(right_node_robbed, right_node_not_robbed)

            return node_robbed, node_not_robbed

        return max(postorder(root))