class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums = sorted(nums)
        def dfs(index):
            if index == len(nums):
                res.append(path.copy())
                return

            path.append(nums[index])
            dfs(index+1)
            path.pop()
            while index < len(nums)-1 and nums[index] == nums[index+1]:
                index+=1
            dfs(index+1)
        dfs(0)
        return res