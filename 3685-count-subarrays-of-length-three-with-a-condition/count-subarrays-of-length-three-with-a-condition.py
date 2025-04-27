class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count=0
        if len(nums)<3:
            return 0
        for i in range(1,len(nums)-1):
            first=nums[i-1]
            second=nums[i]
            third=nums[i+1]
            if second == 2*(first+third):
                count+=1
        return count

            
        
        return count
        