class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = prices[0]
        profit = 0
        for n in prices:
            if n < min_seen:
                min_seen = n   
            profit = max(profit, n - min_seen)
        return profit

        


