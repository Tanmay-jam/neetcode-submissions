class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans=0
        l, r = 1, n
        while l<=r:
            mid = l + (r-l)//2
            if mid*(mid+1)//2<=n:
                ans = max(ans, mid)
                l=mid+1
            else:
                r=mid-1
        return ans