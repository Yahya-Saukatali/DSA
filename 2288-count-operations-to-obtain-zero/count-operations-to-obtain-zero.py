class Solution(object):
    def countOperations(self, num1, num2):
        operations=0
        while num1 and num2 > 0:
            if num1 >= num2:
                num1= num1-num2
                operations+=1
            else:
                num2= num2-num1
                operations+=1
        return operations

