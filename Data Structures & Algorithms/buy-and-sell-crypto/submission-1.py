class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        for right in range(1, len(prices)):
            print(left, right)
            if prices[left] < prices[right]:
                profit = max(profit, prices[right]-prices[left])
            while prices[left] > prices[right] and left < right:
                left+=1
            
        return profit

       