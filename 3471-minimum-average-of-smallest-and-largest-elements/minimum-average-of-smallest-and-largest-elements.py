class Solution(object):
    def minimumAverage(self, nums):
        res=[]
        N=len(nums)
        k= N / 2
        while k > 0:
            average=(min(nums)+max(nums)) / 2.0
            res.append(average)
            nums.remove(min(nums))
            nums.remove(max(nums))
            k-=1
        return min(res)