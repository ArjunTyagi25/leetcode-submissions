"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def rec(node):
            if not node:
                return None

            curr = node
            tail = curr

            while curr:
                tail = curr
                if curr.child:
                    nxt = curr.next
                    chd = curr.child

                    # Updating curr and curr.child to point to each other
                    curr.next = chd
                    chd.prev = curr

                    # Update nxt and tail of child list (chdTail) to point to each other
                    chdTail = rec(curr.child)
                    chdTail.next = nxt
                    if nxt:
                        nxt.prev = chdTail
                    
                    curr.child = None
                    tail = chdTail
                    curr = nxt
                else:
                    curr = curr.next

            return tail

        rec(head)
        return head