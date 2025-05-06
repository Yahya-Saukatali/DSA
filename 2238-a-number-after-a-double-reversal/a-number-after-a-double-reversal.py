class Solution(object):
    def isSameAfterReversals(self, num):
        if num == 0:
            return True
        reversed1=str(num)[::-1]
        reversed1=reversed1.lstrip("0")
        reversed2=reversed1[::-1]
        return str(num)==reversed2