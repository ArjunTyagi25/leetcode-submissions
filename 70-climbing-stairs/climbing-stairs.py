class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def rec(remainingSteps,):
            if remainingSteps == 0:
                return 1

            if remainingSteps < 0:
                return 0

            if remainingSteps in memo:
                return memo[remainingSteps]
            
            res = rec(remainingSteps - 1) + rec(remainingSteps - 2)
            memo[remainingSteps] = res
            return res
    
        return rec(n)
