# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode | None):
        self.root = root
        self.candidateNodes = deque()

        if root:
            q = deque()
            q.append(self.root)

            while q:
                for _ in range(len(q)):
                    node = q.popleft()

                    if not node.left or not node.right:
                        self.candidateNodes.append(node)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)        

    def insert(self, val: int) -> int:
        node = self.candidateNodes[0]

        if not node.left:
            node.left = TreeNode(val)
            self.candidateNodes.append(node.left)
            return node.val
        if not node.right:
            node.right = TreeNode(val)
            _ =  self.candidateNodes.popleft()
            self.candidateNodes.append(node.right)
            return node.val
        
    def get_root(self) -> TreeNode | None:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()