class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # hashSet = {}
        prod_arr = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            prod_arr.append(prod)
        return(prod_arr)
