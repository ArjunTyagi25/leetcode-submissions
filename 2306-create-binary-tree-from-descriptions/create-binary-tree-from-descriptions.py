# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_val_to_node = {}
        node_val_to_parent = {}

        for parent, child, isLeft in descriptions:
            if child in node_val_to_node:
                childNode = node_val_to_node[child]
            else:
                childNode = TreeNode(child)
                node_val_to_node[child] = childNode

            if parent in node_val_to_node:
                parentNode = node_val_to_node[parent]
            else:
                parentNode = TreeNode(parent)
                node_val_to_node[parent] = parentNode

            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode

            node_val_to_parent[child] = parentNode

        for node_val in node_val_to_node:
            if node_val not in node_val_to_parent:
                return node_val_to_node[node_val]

            

        