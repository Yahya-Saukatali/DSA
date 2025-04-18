class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        res=arrivalTime+delayedTime
        if res < 24:
            return res
        elif res > 24:
            res=res % 24
        else:
            return 0
        return res

        