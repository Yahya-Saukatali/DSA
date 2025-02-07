class Solution(object):
    def removeStars(self, s):
        result=[]
        for c in s:
            if c != "*":
                result.append(c)
            elif result:
                result.pop()
        return "".join(result)
       
               
               
                
       