class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        if n == 2: return 2
        o = 1
        t = 2
        for i in range(3, n + 1): o, t = t, t + o
        return t