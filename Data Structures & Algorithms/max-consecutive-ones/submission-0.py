class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        mx_cnt=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            else:
                mx_cnt = max(mx_cnt, cnt)
                cnt=0
        mx_cnt = max(mx_cnt, cnt)
        return mx_cnt