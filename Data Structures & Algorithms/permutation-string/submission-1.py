class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c1, c2 = {}, {}
        for i in range(len(s1)):
            c1[s1[i]] = c1.get(s1[i], 0) + 1
        for i in range(len(s1)):
            c2[s2[i]] = c2.get(s2[i], 0) + 1
        
        for j in range(len(s2)-len(s1)):
            if c1==c2:
                return True
    
            c2[s2[j]]-=1
            if not c2[s2[j]]:
                c2.pop(s2[j])
            c2[s2[j+len(s1)]] = c2.get(s2[j+len(s1)], 0) + 1
        return c1==c2