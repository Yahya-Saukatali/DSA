class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        count={}
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] not in count:
                    count[grid[i][j]]=0
                count[grid[i][j]]+=1
        repeated,missing=0,0
        for num in range(1,len(grid)*len(grid)+1):
            if num not in count:
                missing=num
            elif count[num]==2:
                repeated=num
        return [repeated,missing]