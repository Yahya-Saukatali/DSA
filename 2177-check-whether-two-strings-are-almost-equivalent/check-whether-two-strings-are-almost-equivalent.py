class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        count1=Counter(word1)
        count2=Counter(word2)
        for char in set(word1+word2):
            if abs(count1[char]-count2[char]) >3:
                return False
        return True        