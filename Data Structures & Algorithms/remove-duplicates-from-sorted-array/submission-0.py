class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr=nums[0]
        i, j = 1, 1
        while j<len(nums):
            if nums[j]!=curr:
                nums[i]= nums[j]
                curr = nums[i]
                i+=1
            j+=1
        return i