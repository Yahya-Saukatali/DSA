class Solution(object):
    def distinctAverages(self, nums):
        nums.sort()
        averages=set()
        while len(nums) > 0:
            curr_average=int(min(nums)+max(nums))
            averages.add(curr_average)
            nums.remove(min(nums))
            nums.remove(max(nums))
        return len(averages)
