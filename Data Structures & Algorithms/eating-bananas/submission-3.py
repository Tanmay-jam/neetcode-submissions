class Solution:
    def hours_needed(self, piles, k):
        hours=0
        for p in piles:
            hours+= p//k
            if p%k:
                hours+=1
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = 1, max(piles)
        ans = 0
        while s<=e:
            mid = (e-s)//2 + s
            h_needed = self.hours_needed(piles, mid)
            if h_needed<=h:
                ans = mid
                e = mid-1
            else:
                s = mid+1
        return ans

