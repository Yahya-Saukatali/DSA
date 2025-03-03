class Solution(object):
    def pivotArray(self, nums, pivot):
        smaller_nums=[]
        greater_nums=[]
        for i in nums:
            if i < pivot:
                smaller_nums.append(i) 
            if i > pivot:
                greater_nums.append(i)
        for i in nums:
            if i == pivot:
                smaller_nums.append(i) 
        return smaller_nums + greater_nums
            
