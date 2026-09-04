class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        mySet = set()
        for i in range(len(nums)-1):
            if not ((nums[i]%2==0 and nums[i+1]%2==1) or (nums[i]%2==1 and nums[i+1]%2==0)):
                return False
        return True