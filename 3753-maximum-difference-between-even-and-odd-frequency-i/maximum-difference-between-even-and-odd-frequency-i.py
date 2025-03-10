class Solution(object):
    def maxDifference(self, s):
        freq=Counter(s)
        max_odd=0
        min_even=float('inf')
        for count in freq.values():
            if count % 2 ==1:
                if count > max_odd:
                    max_odd = count
            else:
                if count < min_even:
                    min_even = count
        return max_odd-min_even



        """
        :type s: str
        :rtype: int
        """
        