class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def rec(remaining_amount):
            if remaining_amount == 0:
                return 0

            if remaining_amount < 0:
                return float('inf')

            if remaining_amount in memo:
                return memo[remaining_amount]

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + rec(remaining_amount - coin))
            
            memo[remaining_amount] = res
            return res
        
        res = rec(amount)
        if res == float('inf'):
            return -1
        else:
            return res 