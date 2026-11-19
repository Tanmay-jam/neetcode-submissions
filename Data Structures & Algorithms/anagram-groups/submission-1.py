class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for ele in strs:
            key = ''.join(sorted(ele))
            if key in d:
                d[key].append(ele)
            else:
                d[key]=[ele]
        return list(d.values())