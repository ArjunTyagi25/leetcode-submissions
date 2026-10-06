class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def rec(n):
            if n == 0 or n == 1:
                return 1

            if n in memo:
                return memo[n]

            res = 0
            for i in range(1, n+1):
                res = res + rec(i-1) * rec(n-i)

            memo[n] = res
            return res

        return rec(n)