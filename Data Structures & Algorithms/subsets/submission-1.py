class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        substring = []
        def dfs(i):
            #Base Case
            if i>=len(nums):
                res.append(substring.copy())
                return
            
            #With i search
            substring.append(nums[i])
            dfs(i+1)

            #Without i search
            substring.pop()
            dfs(i+1)

        dfs(0)
        return res