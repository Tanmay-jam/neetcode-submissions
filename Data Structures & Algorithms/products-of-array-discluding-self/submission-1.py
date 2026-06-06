class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preP, postP = [1]*n, [1]*n
        for i in range(1,n):
            preP[i] = preP[i-1]*nums[i-1]
        for j in range(n-2, -1, -1):
            postP[j] = postP[j+1]*nums[j+1]
        ans = []
        for i in range(n):
            ans.append(preP[i]*postP[i])
        return ans
        