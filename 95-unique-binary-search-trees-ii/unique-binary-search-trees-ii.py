# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def rec(start, end):
            if start > end:
                return [None]

            res = []
            for i in range(start, end+1):
                possibleLeftSubtrees = rec(start, i-1)
                possibleRightSubtrees = rec(i+1, end)
                
                for leftSubtree in possibleLeftSubtrees:
                    for rightSubtree in possibleRightSubtrees:
                        node = TreeNode(i)
                        node.left, node.right = leftSubtree, rightSubtree
                        res.append(node)

            return res

        return rec(1, n)


        