class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count=0
        curr_count=0
        for i in nums:
            if i == 1 :
                curr_count+=1
                max_count=max(curr_count,max_count)
            else:
                curr_count=0
        return max_count