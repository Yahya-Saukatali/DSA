import math
class Solution(object):
    def pickGifts(self, gifts, k):
        while k > 0:
            gifts_max_index=gifts.index(max(gifts))
            gifts[gifts_max_index]=int(math.sqrt(gifts[gifts_max_index]))
            k-=1
        return sum(gifts)
                 
        
        



       
        