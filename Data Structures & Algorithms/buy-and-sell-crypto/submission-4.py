class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        l = 0
        for r in range(1, len(prices)):
            sum = prices[r]-prices[l]
            if sum > 0:
                res = max(res, sum)
            else:
                l = r
        return res


       