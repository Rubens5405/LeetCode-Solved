class Solution(object):
    def searchInsert(self, nums, target):
        p = 0
        for i in range(len(nums)):
            if nums[i] == target: p = i; return p 
            elif nums[i] > target: p = i; return p
            if target > nums[i]: p = i + 1
        return p