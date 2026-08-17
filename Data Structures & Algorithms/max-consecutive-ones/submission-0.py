class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for n in nums:
            if n == 0:
                res = max(res, curr)
                curr=0
            else:
                curr+=1
        return max(res, curr)