class Solution:
    def mySqrt(self, x: int) -> int:
        s, e = 1, x
        ans = x
        while s<=e:
            mid = (e-s)//2 + s
            if mid*mid<=x:
                ans = mid
                s = mid+1
            else:
                e = mid-1
        return ans