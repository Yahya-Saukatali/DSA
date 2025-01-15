class Solution(object):
    def sortArrayByParity(self, nums):
        odd_num = []
        even_num = []
        for i in nums:
            if i % 2 == 0:
                even_num.append(i)
            else:
                odd_num.append(i)
        return even_num + odd_num

        