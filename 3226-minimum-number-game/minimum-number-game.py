class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        arr=[]
        N=len(nums)
        for i in range(N):
            arr.append(nums[i])
        for i in range(0,N,2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
        return arr 
            
        