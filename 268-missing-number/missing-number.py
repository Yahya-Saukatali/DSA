class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=set(nums)
        for i in range(n+1):
            if i not in s:
                return i 
        