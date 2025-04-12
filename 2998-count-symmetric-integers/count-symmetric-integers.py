class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count=0
        for i in range(low,high+1):
            sum1=0
            sum2=0
            i=str(i)
            if len(i) % 2==1:
                continue
            mid=len(i)//2
            first_half=i[:mid]
            second_half=i[mid:]
            if sum([int(i) for i in first_half if type(i)== int or i.isdigit()]) == sum([int(i) for i in second_half if type(i)== int or i.isdigit()]):
                count+=1
        return count

        
        