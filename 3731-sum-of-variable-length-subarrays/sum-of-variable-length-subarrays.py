class Solution(object):
    def subarraySum(self, nums):
        res = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            end = i
            res += sum(nums[start:end + 1])
        return res

