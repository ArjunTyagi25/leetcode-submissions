class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def rec(r, c):
            if r == m-1 and c == n-1:
                return 1

            if r > m or c > n:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]

            res = rec(r+1, c) + rec(r, c+1)
            memo[(r,c)] = res
            return res

        return rec(0,0)
        