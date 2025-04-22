class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ant_pos=0
        count=0
        for i in range(len(nums)):
            ant_pos+=nums[i]
            if ant_pos==0:
                count+=1
        return count
        