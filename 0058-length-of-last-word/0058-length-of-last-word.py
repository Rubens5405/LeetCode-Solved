class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        n = 0
        l = len(s) - 1
        while l >= 0 and s[l] != " ": l -= 1; n += 1
        return n
        