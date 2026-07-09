class Solution(object):
    def passwordStrength(self, password):
        password = set(password)
        p = 0
        for c in password:
            if "a" <= c <= "z": p += 1 
            elif "A" <= c <= "Z": p += 2
            elif "0" <= c <= "9": p += 3
            else: p += 5
        return p
        