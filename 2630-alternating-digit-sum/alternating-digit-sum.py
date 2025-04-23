class Solution(object):
    def alternateDigitSum(self, n):
        res=0
        n=[i for i in str(n)]
        for i in range(0,len(n),2):
            res+=int(n[i])
        for i in range(1,len(n),2):
            res-=int(n[i])
        return res