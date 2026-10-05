class Solution:
    def arrangeCoins(self, n: int) -> int:
        strcase=0
        size=1
        while n>=size:
            n-=size
            strcase+=1
            size+=1
        return strcase

