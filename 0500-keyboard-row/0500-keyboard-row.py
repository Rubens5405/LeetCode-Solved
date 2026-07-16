class Solution(object):
    def findWords(self, words):
        l1 = set("qwertyuiop")
        l2 = set("asdfghjkl")
        l3 = set("zxcvbnm")
        r = []
        for w in words:
            l = set(w.lower())
            if l <= l1 or l <= l2 or l <= l3: r.append(w)
        return r
        