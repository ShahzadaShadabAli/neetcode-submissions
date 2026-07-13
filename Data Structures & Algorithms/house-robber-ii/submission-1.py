class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first = self.robber(nums[1:])
        second = self.robber(nums[:-1])
        return max(first, second)
    def robber(self, nums):
        rob1, rob2 = 0, 0
        for n in (nums):
            temp = max(rob2, rob1+n)
            rob1 = rob2
            rob2 = temp
        return rob2