class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        m = 0
        a = 0
        for n in nums:
            if n == 1:
                a += 1
                if a > m: m = a
            else: a = 0
        return m