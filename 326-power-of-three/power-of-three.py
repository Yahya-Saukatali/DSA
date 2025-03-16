class Solution(object):
    def isPowerOfThree(self, n):
        for i in range(31):
            if n == 3**i:
                return True
        return False
            