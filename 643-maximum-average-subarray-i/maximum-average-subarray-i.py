class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum=sum(nums[:k])
        max_avg=curr_sum / float(k)
        for i in range(k,len(nums)):
            curr_sum+=nums[i]
            curr_sum-=nums[i-k]
            curr_avg=curr_sum / float(k)
            max_avg=max(curr_avg,max_avg)
        return max_avg
