# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        n = len(nums)

        def rec(L, R):
            if L==R:
                return TreeNode(nums[L])
            elif L + 1 == R:
                right_node = TreeNode(nums[R])
                return TreeNode(nums[L], None, right_node)

            M = (L+R)//2
            left_subtree = rec(L, M-1)
            right_subtree = rec(M+1, R)
            return TreeNode(nums[M], left_subtree, right_subtree)

        return rec(0, n-1)

        