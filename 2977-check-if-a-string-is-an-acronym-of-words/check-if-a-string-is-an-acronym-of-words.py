class Solution(object):
    def isAcronym(self, words, s):
        string=''
        for i in range(len(words)):
            string+=words[i][0]
        #string.append(i[0])
        return string==s
