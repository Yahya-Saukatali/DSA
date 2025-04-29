class Solution(object):
    def kthDistinct(self, arr, k):
        Count=Counter(arr)
        distinct=[i for i in arr if Count[i]==1]
        if k > len(distinct):
            return ""
        else:
            return distinct[k-1]



        