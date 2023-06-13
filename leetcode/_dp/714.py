from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        max_buy = -prices[0]-fee
        max_sell = 0

        for i in range(1, n):
            new_buy = max_sell - prices[i] - fee
            new_sell = max_buy + prices[i]
            max_buy = max(max_buy, new_buy)
            max_sell = max(max_sell, new_sell)
        return max_sell