class Solution(object):
    def checkIfPangram(self, sentence):
        alphabets="abcdefghijklmnopqrstuvwxyz"
        alphabets=list(alphabets)
        for i in sentence:
            if i in alphabets:
                alphabets.remove(i)
       
        return alphabets == []
