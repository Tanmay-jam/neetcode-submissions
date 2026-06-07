class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, h = i+1, len(nums)-1
            while l<h:
                if nums[l] + nums[h] == -nums[i]:
                    ans.append([nums[i], nums[l], nums[h]])
                    l+=1
                    while nums[l] == nums[l-1] and l<h:
                        l+=1
                elif nums[l] + nums[h] < -nums[i]:
                    l+=1
                else:
                    h-=1
        return ans
                