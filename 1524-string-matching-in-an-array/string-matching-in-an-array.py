class Solution(object):
    def stringMatching(self, words):
        res = []
        N = len(words)
        for i in range(N):
            for j in range(N):
                if i==j:
                    continue
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res


        