class Solution(object):
    def maxFreqSum(self, s):
        vowels=set('aeiou')
        freq=Counter(s)
        max_vowel=0
        max_cons=0
        for char ,count in freq.items():
            if char in vowels:
                max_vowel=max(max_vowel,count)
            elif char.isalpha():
                max_cons=max(max_cons,count)
        return max_vowel+max_cons