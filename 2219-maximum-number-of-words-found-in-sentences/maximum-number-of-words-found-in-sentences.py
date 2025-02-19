class Solution(object):
    def mostWordsFound(self, sentences):
        res = 0
        for sentence in sentences:
            res = max(res, len(sentence.split()))
        return res 



