class Solution(object):
    def getSneakyNumbers(self, nums):
        nums2=set()
        res=[]
        for i in nums:
            if i in nums2:
                res.append(i)
            else:
                nums2.add(i)
        return res
