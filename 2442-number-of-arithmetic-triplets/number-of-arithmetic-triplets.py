class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        n=len(nums)
        for i in range(n-2):
            l=i+1
            r=n-1
            while l < r:
                if nums[l] - nums[i] == diff and nums[r] - nums[l] == diff:
                    count+=1
                    l+=1
                    r-=1
                elif nums[l]-nums[i] < diff:
                    l+=1
                else:
                    r-=1
        return count

        