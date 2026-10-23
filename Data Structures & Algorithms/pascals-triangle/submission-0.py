class Solution:
    def fact(self, num):
        if num==0:
            return 1
        return num*self.fact(num-1)

    def comb(self, n, r):
        return self.fact(n)//(self.fact(n-r)*self.fact(r))

    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(self.comb(i,j))
            ans.append(temp)
        return ans