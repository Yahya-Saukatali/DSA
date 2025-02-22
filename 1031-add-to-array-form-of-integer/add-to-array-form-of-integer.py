class Solution(object):
    def addToArrayForm(self, num, k):
        num=int(''.join(map(str,num)))
        num+=k
        return [int(i) for i in str(num)]
