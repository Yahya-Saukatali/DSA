class Solution(object):
    def finalPrices(self, prices):
        res = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    res.append(prices[i] - prices[j])
                    break
            else:
                res.append(prices[i])
        return res

