class Solution(object):
    def reversePrefix(self, word, ch):
        res=''
        i=word.find(ch)
        if i ==-1:
            return word
        return word[:i+1][::-1]+word[i+1:]
            

        