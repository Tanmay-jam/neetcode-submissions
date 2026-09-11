class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt={}
        for ele in nums:
            if ele not in cnt and len(cnt)==2:
                new_cnt = {}
                for k in cnt.keys():
                    if cnt[k]>1:
                        new_cnt[k] = cnt[k]-1
                cnt = new_cnt
            else:
                cnt[ele] = cnt.get(ele, 0) + 1
        l = len(nums)
        res=[]
        for k in cnt:
            if nums.count(k)>l//3:
                res.append(k)
        return res



