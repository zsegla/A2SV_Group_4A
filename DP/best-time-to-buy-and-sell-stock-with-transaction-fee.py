# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/



class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = float("-inf"), 0

        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy +price - fee)
        return sell
