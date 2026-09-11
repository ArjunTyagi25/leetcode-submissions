class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def rec(remaining_amount, curr_coin_idx):
            if remaining_amount == 0:
                return 1

            if remaining_amount < 0 or curr_coin_idx == len(coins):
                return 0

            if (remaining_amount, curr_coin_idx) in memo:
                return memo[(remaining_amount, curr_coin_idx)]

            skip = rec(remaining_amount, curr_coin_idx+1)
            take = rec(remaining_amount - coins[curr_coin_idx], curr_coin_idx)
            total_ways = skip + take

            memo[(remaining_amount, curr_coin_idx)] = total_ways
            return total_ways

        return rec(amount, 0)