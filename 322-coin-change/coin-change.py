class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def rec(cur_amount):
            if cur_amount == 0:
                return 0

            if cur_amount < 0:
                return float('inf')

            if cur_amount in memo:
                return memo[cur_amount]

            min_coin = float('inf')
            for coin in coins:
                min_coin = min(min_coin, rec(cur_amount - coin))

            memo[cur_amount] = 1 + min_coin
            return memo[cur_amount]

        res = rec(amount)
        if res == float('inf'):
            return -1
        else:
            return res

        