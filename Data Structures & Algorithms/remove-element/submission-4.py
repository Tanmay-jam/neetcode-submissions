class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt=0
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                cnt+=1
                i+=1
        return cnt