class Solution(object):
    def uniqueOccurrences(self, arr):
        count=Counter(arr)
        s=set()
        for v in count.values():
            if v in s:
                return False
            else:
                s.add(v)
        return True
        