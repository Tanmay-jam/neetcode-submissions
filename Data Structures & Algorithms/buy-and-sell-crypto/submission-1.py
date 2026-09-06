class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        i=0
        for j in range(1, len(prices)):
            maxprofit = max(maxprofit, prices[j]-prices[i])
            if prices[j]<prices[i]:
                i=j
        return maxprofit