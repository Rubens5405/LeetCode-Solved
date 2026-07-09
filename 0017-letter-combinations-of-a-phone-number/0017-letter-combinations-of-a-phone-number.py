class Solution(object):
    def letterCombinations(self,digits):
        n={ "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        out=[""]
        for d in digits:
            r=[]
            for c in out:
                for l in n[d]:r.append(c+l)
            out=r 
        return out
        