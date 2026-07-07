class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path, sum):
            if sum == target:
                res.append(path.copy())
                return 
            
            if i == len(nums) or sum > target:
                return
           
            path.append(nums[i])
            dfs(i, path, nums[i]+sum)

            path.pop()
            dfs(i+1, path, sum)
        dfs(0, [], 0)
        return res
