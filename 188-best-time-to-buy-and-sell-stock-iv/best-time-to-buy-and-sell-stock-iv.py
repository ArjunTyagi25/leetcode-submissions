class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        memo = {}
        def rec(currDay, isHolding, numTransactions):
            if currDay == len(prices):
                return 0

            if numTransactions > k:
                return 0

            state = (currDay, isHolding, numTransactions)
            if state in memo:
                return memo[state]

            # I am already holding a share so I can either sell it today or don't do anything
            if isHolding:
                res_1 = prices[currDay] + rec(currDay + 1, False, numTransactions)
                res_2 = rec(currDay + 1, isHolding, numTransactions)
                res = max(res_1, res_2)
                memo[state] = res
                return res
            # I am not holding a share so I can either buy today or don't do anything
            else:
                res_1 = 0
                if numTransactions < k:
                    res_1 = -prices[currDay] + rec(currDay + 1, True, numTransactions + 1)
                res_2 = rec(currDay + 1, False, numTransactions)
                res = max(res_1, res_2)
                memo[state] = res
                return res

        return rec(0, False, 0)