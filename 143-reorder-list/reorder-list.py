# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        prev, curr = None, second_half

        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t

        first_half, second_half = head, prev

        while second_half:
            t1 = first_half.next
            first_half.next = second_half
            t2 = second_half.next
            second_half.next = t1

            first_half, second_half = t1, t2

        
        
        