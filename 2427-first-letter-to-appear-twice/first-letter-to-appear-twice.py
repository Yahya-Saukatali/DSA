class Solution(object):
    def repeatedCharacter(self, s):
        seen_elements=[]
        for i in s:
            if i in seen_elements:
                return i
            seen_elements.append(i)
