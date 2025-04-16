class Solution(object):
    def minElement(self, nums):
        res=[]
        for i in nums:
            res.append(sum(map(int,str(i))))
        return min(res)
        
