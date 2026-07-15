def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        odd = 0
        even = 0
        for i in range(1, n + 1):
            odd += i * 2 - 1 
            even += i * 2    
        return gcd(odd, even)