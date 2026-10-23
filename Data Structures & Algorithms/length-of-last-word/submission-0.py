class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        ans=0
        s = s.rstrip()
        for i in range(len(s)):
            if s[i]==" ":
                ans=l
                l=0
            else:
                l+=1
        return l