class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxCount = 0
        count = 0
        nums = set(nums)
        for n in nums:
            if not n-1 in nums:
                while n+count in nums:
                    count += 1
            maxCount = max(count, maxCount)
            count = 0
        return maxCount