class Solution:
    def mySqrt(self, x: int) -> int:
        s, e = 0, x
        while s<=e:
            mid = (e-s)//2 + s
            square = mid*mid
            if square==x:
                return mid
            elif square<x:
                s=mid+1
            else:
                e=mid-1
        return min(s,e)