class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def rec(head, step, remaining, leftToRight):
            if remaining == 1:
                return head

            if leftToRight:
                return rec(head + step, step*2, remaining//2, not leftToRight)
            else:
                if remaining%2 == 0:
                    return rec(head, step*2, remaining//2, not leftToRight)
                else:
                    return rec(head + step, step*2, remaining//2, not leftToRight)
        
        return rec(1, 1, n, True)