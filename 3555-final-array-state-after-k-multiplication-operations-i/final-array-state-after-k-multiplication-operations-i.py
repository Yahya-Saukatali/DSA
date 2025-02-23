class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        count = 0
        while count < k:
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
            count += 1
        return nums

  
        
        

       
