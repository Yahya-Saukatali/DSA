class Solution(object):
    def maxAscendingSum(self, nums):
        cur_sum=nums[0]
        res=cur_sum
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                cur_sum+=nums[i]
            else:
                cur_sum=nums[i]
            res=max(cur_sum,res)
        return res

