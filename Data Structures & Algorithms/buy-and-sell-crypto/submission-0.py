class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        buy = None

        for i in range(len(prices)):
            if buy == None or buy > prices[i]:
                buy = prices[i]
                l = i

            profit = max(profit, prices[i] - buy)

        return profit    
            