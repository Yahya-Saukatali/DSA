class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        n = len(nums)
        count = 0

        def countPairs(bound):
            left, right = 0, n - 1
            total = 0
            while left < right:
                if nums[left] + nums[right] <= bound:
                    total += right - left
                    left += 1
                else:
                    right -= 1
            return total

        return countPairs(upper) - countPairs(lower - 1)
