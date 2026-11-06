class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        while True:
            if nums[i]<0:
                return i
            prev=i
            i=nums[i]
            nums[prev]*=-1