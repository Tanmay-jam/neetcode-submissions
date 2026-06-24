class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        newWord=[]
        while i<min(len(word1), len(word2)):
            newWord.append(word1[i])
            newWord.append(word2[i])
            i+=1
        while i<len(word1):
            newWord.append(word1[i])
            i+=1
        while i<len(word2):
            newWord.append(word2[i])
            i+=1
        return "".join(newWord)