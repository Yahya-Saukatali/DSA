class Solution(object):
    def maxPower(self, s):
        count=1
        max_count=0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                max_count=max(count,max_count)
                count=1
                
        return max(count,max_count)
