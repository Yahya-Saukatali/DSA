class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        res = []
        for word in words:
            res.append(word[::-1])
        return ' '.join(res)
