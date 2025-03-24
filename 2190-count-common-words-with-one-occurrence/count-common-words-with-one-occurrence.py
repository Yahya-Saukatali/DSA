class Solution(object):
    def countWords(self, words1, words2):
        count1=Counter(words1)
        count2=Counter(words2)
        count=0
        for i in count1:
            if count1[i]==1 and count2[i]==1:
                count+=1
        return count


       
        