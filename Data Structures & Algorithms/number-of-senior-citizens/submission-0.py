class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt=0
        for ele in details:
            if int(ele[-4:-2])>60:
                cnt+=1
        return cnt