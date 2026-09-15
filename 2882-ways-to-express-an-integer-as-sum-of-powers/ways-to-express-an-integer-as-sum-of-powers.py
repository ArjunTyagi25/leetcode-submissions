class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        memo = {}
        def rec(remaining, i):
            if remaining == 0:
                return 1

            if remaining < 0:
                return 0

            if pow(i, x) > remaining:
                return 0

            if (remaining, i) in memo:
                return memo[(remaining, i)]

            res = rec(remaining - pow(i, x), i+1) + rec(remaining, i+1)
            memo[(remaining, i)] = res
            return res

        return rec(n, 1)%(10**9 + 7)
        