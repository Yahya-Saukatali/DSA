class Solution(object):
    def generateKey(self, num1, num2, num3):
        s1= '0'*(4-len(str(num1))) + str(num1)
        s2= '0'*(4-len(str(num2))) + str(num2)
        s3= '0'*(4-len(str(num3))) + str(num3)
        res=''
        for i in range(4):
            res+=min(s1[i],s2[i],s3[i])
            

        return int(res)
        