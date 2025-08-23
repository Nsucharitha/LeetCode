class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxprofit = 0

        for i in range(len(prices)-1):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                maxprofit = max(profit, maxprofit)
                r += 1

        return maxprofit 

        