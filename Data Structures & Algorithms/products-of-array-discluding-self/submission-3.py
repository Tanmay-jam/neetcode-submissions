class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1]*len(nums), [1]*len(nums)
        j=len(nums)-2
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
            post[j] = post[j+1]*nums[j+1]
            j-=1
        
        for i in range(len(nums)):
            pre[i]*=post[i]
        return pre

