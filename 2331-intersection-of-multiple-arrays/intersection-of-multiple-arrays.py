class Solution(object):
    def intersection(self, nums):
        result = set(nums[0])
        for lst in nums[1:]:
            result = result.intersection(set(lst))
        return sorted(list(result))
