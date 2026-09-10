class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def rec(remaining_sum):
            if remaining_sum < 0:
                return float('inf')

            if remaining_sum in memo:
                return memo[remaining_sum]

            if remaining_sum == 0:
                return 0

            res = float('inf')
            for i in range(1, int(sqrt(remaining_sum))+1):
                res = min(res, 1 + rec(remaining_sum - i*i))

            memo[remaining_sum] = res
            return res

        return rec(n)
        