class Solution(object):
    def isHappy(self, n):
        h = set() 
        while n != 1:
            if n in h: return False
            h.add(n)
            n = sum(int(digito) ** 2 for digito in str(n))
        return True