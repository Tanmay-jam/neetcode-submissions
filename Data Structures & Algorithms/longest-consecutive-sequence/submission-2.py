class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        cons=1
        max_cons=1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                cons+=1
            elif nums[i]==nums[i-1]:
                pass
            else:
                cons=1
            max_cons = max(max_cons, cons)
        return max_cons