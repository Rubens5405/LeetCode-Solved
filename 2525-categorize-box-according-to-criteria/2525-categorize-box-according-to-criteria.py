class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        v = length * width * height
        box = "" 
        if max(length, width, height) >= 10**4 or v >= 10**9:            
            box = "Bulky"
        if mass >= 100:
            if box == "Bulky":
                box = "Both"
            else:
                box = "Heavy"
        else: 
            if box != "Bulky" and box != "Both":
                box = "Neither"
        return box