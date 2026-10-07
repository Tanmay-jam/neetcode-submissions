class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums)-1
        ans = nums[0]
        while s<=e:
            mid = (e+s)//2
            if nums[0]<=nums[mid]:
                s = mid+1
            elif nums[0]>nums[mid]:
                ans = min(ans, nums[mid])
                e = mid-1
        return ans