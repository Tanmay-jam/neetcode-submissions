class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)-1
        while j>=0 and nums[j]==2:
            j-=1
        
        k=i
        while k<=j:
            if nums[k]==0:
                nums[i], nums[k] = nums[k], nums[i]
                i+=1
                k+=1
            elif nums[k]==2:
                nums[k], nums[j] = nums[j], nums[k]
                j-=1
            else:
                k+=1