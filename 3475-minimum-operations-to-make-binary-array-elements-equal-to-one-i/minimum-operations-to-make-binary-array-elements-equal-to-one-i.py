class Solution(object):
    def minOperations(self, nums):
        count=0
        i=0
        n=len(nums)
        while i <= n-3:
            if nums[i]==0:
                nums[i]=1
                nums[i+1]^=1
                nums[i+2]^=1
                count+=1
            i+=1
        if all(num==1 for num in nums):
            return count
        else:
            return -1
