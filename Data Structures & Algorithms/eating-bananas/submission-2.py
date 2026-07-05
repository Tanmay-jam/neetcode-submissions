class Solution:
    def hours_req(self, piles, k):
        hours = 0
        for i in range(len(piles)):
            hours += piles[i]//k
            if piles[i]%k:
                hours+=1
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = 1, max(piles)
        ans = max(piles)
        while s<=e:
            mid = (e-s)//2 + s
            if self.hours_req(piles, mid)<=h:
                ans = mid
                e = mid-1
            else:
                s = mid+1
        return ans