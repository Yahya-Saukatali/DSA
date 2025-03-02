class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        count = Counter()
        items = items1 + items2
        for key, value in items:
            count[key] += value
            
        return sorted(count.items())
