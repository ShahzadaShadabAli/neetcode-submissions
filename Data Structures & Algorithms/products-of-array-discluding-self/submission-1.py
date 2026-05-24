class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        fix = 1
        for i in range(len(nums)):
            output.append(fix)
            fix*=nums[i]
        fix = 1
        for j in range(len(nums), 0, -1):
            output[j-1] *= fix
            fix *= nums[j-1]
        return output
