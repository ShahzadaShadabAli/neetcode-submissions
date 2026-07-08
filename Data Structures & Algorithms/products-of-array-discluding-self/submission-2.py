class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        fix = 1

        for i in range(len(nums)):
            res.append(fix)
            fix *= nums[i]
        fix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j]*=fix
            fix*=nums[j]
        return res