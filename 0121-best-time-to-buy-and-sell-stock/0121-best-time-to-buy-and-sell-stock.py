class Solution(object):
    def maxProfit(self, prices):

        maxProfit = 0
        bestBuy = prices[0]

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - bestBuy)
            bestBuy = min(bestBuy, prices[i])
        
        return maxProfit