class Solution(object):
    def findNumbers(self, nums):
        res=0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2==0:
                res+=1
        return res
        