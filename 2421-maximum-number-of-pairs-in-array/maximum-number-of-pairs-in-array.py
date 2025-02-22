from collections import Counter

class Solution(object):
    def numberOfPairs(self, nums):
        count = Counter(nums)  
        pairs = 0
        singles = 0

        for value in count.values():
            pairs += value // 2      
            singles += value % 2     

        return [pairs, singles]
