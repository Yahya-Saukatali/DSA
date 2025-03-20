class Solution(object):
    def findJudge(self, n, trust):
        incoming =defaultdict(int)
        outgoing =defaultdict(int)
        for src,dst in trust:
            incoming[dst]+=1
            outgoing[src]+=1
        for i in range(1, n+1):
            if outgoing[i]==0 and incoming[i]==n-1:
                return i
        return -1 

        