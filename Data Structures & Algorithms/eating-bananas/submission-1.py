class Solution:
    def hours_needed(self, piles, eat_speed):
        h_needed = 0
        for i in range(len(piles)):
            h_needed += piles[i]//eat_speed
            if piles[i]%eat_speed:
                h_needed += 1
        return h_needed

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = 1, max(piles)
        minrate = None
        while s<=e:
            mid = s + (e-s)//2
            h_needed = self.hours_needed(piles, mid)
            if h_needed <= h:
                minrate = mid
                e = mid-1
            else:
                s = mid + 1  
        return minrate
