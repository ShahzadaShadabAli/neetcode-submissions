class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        resArr = [1]*len(nums)
        for i in range(len(resArr)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    resArr[i] = max(resArr[i], resArr[j]+1)
        return max(resArr)