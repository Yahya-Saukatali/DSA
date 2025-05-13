class Solution(object):
    def largestInteger(self, num):
        num_str = str(num)
        even_digits = sorted([int(d) for d in num_str if int(d) % 2 == 0], reverse=True)
        odd_digits = sorted([int(d) for d in num_str if int(d) % 2 != 0], reverse=True)
        result = ""
        for d in num_str:
            if int(d) % 2 == 0:
                result += str(even_digits.pop(0))
            else:
                result += str(odd_digits.pop(0))
        return int(result)
