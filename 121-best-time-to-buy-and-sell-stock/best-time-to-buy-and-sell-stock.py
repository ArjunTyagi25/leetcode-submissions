class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = float('inf')
        buying_day = -1
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < buying_price:
                buying_price = prices[i]
                buying_day = i
            else:
                if i > buying_day:
                    max_profit = max(max_profit, prices[i] - buying_price)

        return max_profit
            