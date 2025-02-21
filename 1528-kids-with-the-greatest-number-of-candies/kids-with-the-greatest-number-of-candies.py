class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res

