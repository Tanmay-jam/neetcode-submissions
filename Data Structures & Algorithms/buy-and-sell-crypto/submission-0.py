class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pr = 0
        i=0
        j=1
        while j<len(prices):
            if prices[j]>prices[i]:
                max_pr = max(max_pr, prices[j]-prices[i])
            else:
                i=j
            j+=1
        return max_pr