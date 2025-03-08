class Solution(object):
    def countDigits(self, num):
        count = 0
        arr = [int(x) for x in str(num)]
        for i in arr:
            if num % i == 0:
                count += 1
        return count
