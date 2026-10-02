class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, curr, twos = 0, 0, len(nums)-1
        while curr<=twos:
            if nums[curr]==0:
                nums[zeros], nums[curr] = nums[curr], nums[zeros]
                zeros+=1
                curr+=1
            elif nums[curr]==2:
                nums[twos], nums[curr] = nums[curr], nums[twos]
                twos-=1
            else:
                curr+=1