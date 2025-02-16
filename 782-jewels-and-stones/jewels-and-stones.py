class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        jewels=set([i for i in jewels])
        for s in stones:
            if s in jewels:
                c+=1
        return c

       
        