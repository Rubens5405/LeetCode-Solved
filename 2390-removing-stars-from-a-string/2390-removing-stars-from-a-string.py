class Solution(object):
    def removeStars(self,s):
        a=[]
        for c in s:
            if c!="*":a.append(c)
            else:a.pop()
        return "".join(a)
       