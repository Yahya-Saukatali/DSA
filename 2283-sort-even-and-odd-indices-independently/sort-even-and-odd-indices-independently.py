class Solution(object):
    def sortEvenOdd(self, nums):
        even = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        odd = [nums[i] for i in range(len(nums)) if i % 2 != 0]

        even.sort()
        odd.sort(reverse=True)

        result = []
        even_ptr, odd_ptr = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[even_ptr])
                even_ptr += 1
            else:
                result.append(odd[odd_ptr])
                odd_ptr += 1

        return result

