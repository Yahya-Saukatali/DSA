class Solution(object):
    def findGCD(self, nums):
        largest_num=max(nums)
        smallest_num=min(nums)
        res=[]
        for i in range(1,largest_num+1):
            if largest_num % i == 0 and smallest_num % i ==0:
                res.append(i)
        return max(res)
