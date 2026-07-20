class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        max_len=0
        cnt={}
        for j in range(len(s)):
            cnt[s[j]] = cnt.get(s[j], 0) + 1
            replacable = (j-i+1) - max(cnt.values())

            while replacable>k:
                cnt[s[i]]-=1
                i+=1
                replacable = (j-i+1) - max(cnt.values())

            max_len = max(max_len, j-i+1)
        return max_len