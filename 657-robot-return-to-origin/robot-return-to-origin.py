class Solution(object):
    def judgeCircle(self, moves):
        x=0
        y=0
        for i in moves:
            if i == 'L':
                x-=1
            elif i == 'R':
                x+=1
            elif i == 'U':
                y+=1
            elif i == 'D':
                y-=1
        return x==0 and y==0
         

        