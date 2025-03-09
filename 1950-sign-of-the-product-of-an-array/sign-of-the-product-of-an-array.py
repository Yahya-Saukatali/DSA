class Solution(object):
    def arraySign(self, nums):
        negative_count=0
        for num in nums:
            if num ==0:
                return 0
            if num < 0:
                negative_count+=1

        return 1 if negative_count % 2==0 else -1
        