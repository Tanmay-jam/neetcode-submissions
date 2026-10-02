class Solution:
    def isValid(self, s: str) -> bool:
        par = {')':'(', ']':'[', '}':'{'}
        stk = []
        if not s:
            return True
        for ele in s:
            if ele in par.values():
                stk.append(ele)
            elif ele in par.keys():
                if not stk:
                    return False
                elif stk[-1]==par[ele]:
                    stk.pop(-1)
                else:
                    return False
        if stk:
            return False
        return True 