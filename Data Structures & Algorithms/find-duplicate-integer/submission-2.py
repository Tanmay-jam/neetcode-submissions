class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nmap=set()
        for ele in nums:
            if ele in nmap:
                return ele
            nmap.add(ele)