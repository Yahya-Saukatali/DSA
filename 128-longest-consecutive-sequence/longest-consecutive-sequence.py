class Solution(object):
    def longestConsecutive(self, nums):
        if nums==[] : return 0
        nums=list(set(nums))
        nums.sort()
        count=1
        longest=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
                longest=max(count,longest)
            else:
                count=1
        return longest

        