class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total, res = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                total += nums[i]
            else:
                res = max(res, total)
                total = nums[i]
            res = max(res, total)
        return res