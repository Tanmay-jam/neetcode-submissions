class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        seen = set()
        l, longest = 0, 0
        for j in range(len(s)):
            l+=1
            while s[j] in seen:
                seen.remove(s[i])
                i+=1
                l-=1
            longest = max(longest, l)
            seen.add(s[j]) #seen[s[j]]=j
        return longest
