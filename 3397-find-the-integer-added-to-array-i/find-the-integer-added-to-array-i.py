class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res=0
        for i in range(len(nums1)):
            res=nums2[i]-nums1[i]
        return res
