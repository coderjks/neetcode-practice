class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for cur_price in prices:
            max_profit = max(cur_price - min_price, max_profit)
            min_price = min(min_price, cur_price)
        
        return max_profit