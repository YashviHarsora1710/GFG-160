class Solution:
    def maximumProfit(self, prices):
        # code here
        max_profit=0
        min_price=prices[0]
        
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            profit=prices[i]-min_price
            max_profit=max(profit,max_profit)
        return max_profit