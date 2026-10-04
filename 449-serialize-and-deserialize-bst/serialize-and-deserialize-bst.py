# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""

        inorderVals = []
        postorderVals = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            inorderVals.append(str(node.val))
            inorder(node.right)

        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)
            postorderVals.append(str(node.val))

        inorder(root)
        postorder(root)

        res = ",".join(inorderVals) + ";" + ",".join(postorderVals)
        return res
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None

        inorder, postorder = data.split(";")[0].split(","), data.split(";")[1].split(",")
        inorderIndex = { inorder[i] : i for i in range(len(inorder))}

        def createBST(L, R):
            if L > R:
                return None

            if postorder:
                node = TreeNode(postorder.pop())
                index = inorderIndex[node.val]
                node.right = createBST(index+1, R)
                node.left = createBST(L, index-1)

                return node

        return createBST(0, len(inorder) - 1)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans