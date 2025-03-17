class Solution(object):
    def divideArray(self, nums):
        count=Counter(nums)
        for i in count.values():
            if i % 2 != 0:
                return False
        return True

