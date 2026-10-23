class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            case= words[i]
            for j in range(len(words)):
                if j!=i and (case in words[j]):
                    ans.append(case)
                    break
        return ans