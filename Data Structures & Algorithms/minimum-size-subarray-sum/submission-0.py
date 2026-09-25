class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j = 0,0
        min_l, s = len(nums)+1, 0
        for j in range(len(nums)):
            s+=nums[j]
            while s>=target:
                min_l = min(min_l, j-i+1)
                s-=nums[i]
                i+=1
        if min_l==len(nums)+1:
            return 0
        return min_l