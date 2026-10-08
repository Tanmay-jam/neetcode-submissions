class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        j=0
        for i in range(len(nums)):
            if i-j>k:
                seen.remove(nums[j])
                j+=1
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
            
            