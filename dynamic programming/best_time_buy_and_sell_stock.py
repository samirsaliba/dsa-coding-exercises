# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] 
# is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                # new minfound
                min_price = prices[i]

            elif prices[i] - min_price > max_profit:
                # new max profit found
                max_profit = prices[i] - min_price
            
        return max_profit