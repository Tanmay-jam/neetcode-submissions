class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        i, j = 0, 1
        for j in range(1, len(prices)):
            if prices[i]<prices[j]:
                profit += (prices[j]-prices[i])
            i=j
        return profit
