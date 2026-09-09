class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1]*len(nums), [1]*len(nums)
        for i in range(len(nums)):
            pre[i] = pre[i-1]*nums[i-1] if i>0 else 1
        for i in range(len(nums)-1, -1, -1):
            post[i] = post[i+1]*nums[i+1] if i<len(nums)-1 else 1
        
        op=[]
        for i in range(len(nums)):
            op.append(pre[i]*post[i])
        return op