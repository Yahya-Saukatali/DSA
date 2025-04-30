class Solution(object):
    def addSpaces(self, s, spaces):
        res=[]
        last_index=0
        for i in spaces:
            res.append(s[last_index:i])
            res.append(" ")
            last_index=i
        res.append(s[last_index:])
        return ''.join(res)

