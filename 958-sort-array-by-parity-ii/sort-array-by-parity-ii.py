class Solution(object):
    def sortArrayByParityII(self, nums):
        even_index, odd_index = 0, 1
        res = [0] * len(nums)
        for num in nums:
            if num % 2 == 0:
                res[even_index] = num
                even_index += 2
            else:
                res[odd_index] = num
                odd_index += 2
        return res
