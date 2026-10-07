class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums)-1
        while s<=e:
            mid = s + (e-s)//2
            if nums[mid]==target:
                return mid
            elif nums[s]<=nums[mid]: #left half sorted
                if nums[s]<=target and target<nums[mid]:
                    e=mid-1
                else:
                    s=mid+1
            else: #right half sorted
                if nums[mid]<target and target<=nums[e]:
                    s=mid+1
                else:
                    e=mid-1
        return -1