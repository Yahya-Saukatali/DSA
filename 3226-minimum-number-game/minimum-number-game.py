class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        N=len(nums)
        for i in range(0,N,2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums 
            
        