class Solution(object):
    def halvesAreAlike(self, s):
        vowels = set('aeiouAEIOU')
        count1 = sum(1 for i in s[:len(s)//2] if i in vowels)
        count2 = sum(1 for j in s[len(s)//2:] if j in vowels)
        return count1 == count2
