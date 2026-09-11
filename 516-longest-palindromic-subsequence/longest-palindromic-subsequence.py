class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def rec(L, R):
            if L > R:
                return 0

            if L == R:
                return 1

            if (L,R) in memo:
                return memo[(L,R)]

            res = float('-inf')
            if s[L] == s[R]:
                res = max(res, 2 + rec(L+1, R-1))
            else:
                res = max(res, rec(L+1, R), rec(L, R-1))

            memo[(L,R)] = res
            return res

        return rec(0, len(s)-1)
            
        