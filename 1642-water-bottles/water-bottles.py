class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        result=0
        empty=0
        while numBottles>0:
            result+=numBottles
            empty+=numBottles
            numBottles=empty//numExchange
            empty=empty % numExchange
        return result

        






    