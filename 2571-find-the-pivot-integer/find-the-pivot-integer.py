class Solution(object):
    def pivotInteger(self, n):
        total_sum=sum(range(n+1))
        left_sum=0
        for i in range(n+1):
            right_sum=total_sum-left_sum-i
            if left_sum==right_sum:
                return i
            left_sum+=i
        return -1
            
        
        