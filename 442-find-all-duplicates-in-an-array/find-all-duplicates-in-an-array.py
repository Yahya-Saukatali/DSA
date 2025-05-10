class Solution(object):
    def findDuplicates(self, nums):
        duplicates=[]
        seen=set()
        for i in nums:
            if i in seen:
                duplicates.append(i)
            else:
                seen.add(i)
        return duplicates        