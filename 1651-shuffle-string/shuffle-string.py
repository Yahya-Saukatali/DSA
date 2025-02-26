class Solution(object):
    def restoreString(self, s, indices):
        res=""
        for i in range(len(indices)):
            res+= s[indices.index(i)]
        return res