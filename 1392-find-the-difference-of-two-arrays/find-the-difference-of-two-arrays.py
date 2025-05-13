class Solution(object):
    def findDifference(self, nums1, nums2):
        answer1=set()
        answer2=set()
        for i in nums1:
            if i not in nums2:
                answer1.add(i)
        for i in nums2:
            if i not in nums1:
                answer2.add(i)
        return [list(answer1),list(answer2)]
