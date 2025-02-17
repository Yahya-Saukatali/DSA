#sliding wondow basic
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        stringset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in stringset:
                stringset.remove(s[l])
                l+=1
            stringset.add(s[r])
            res=max(res,r-l+1)
        return res



                
        
        