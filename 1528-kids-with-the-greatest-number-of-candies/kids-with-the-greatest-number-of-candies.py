class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res

