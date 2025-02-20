class Solution(object):
    def isPossibleToSplit(self, nums):
        counting=Counter(nums)
        for count in counting.values():
            if count > 2:
                return False
        return True