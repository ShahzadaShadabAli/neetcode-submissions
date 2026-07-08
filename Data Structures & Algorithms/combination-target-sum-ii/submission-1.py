class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates = sorted(candidates)
        def dfs(index, sum):
            if sum == target:
                res.append(path.copy())
                return

            if sum > target or index == len(candidates):
                return 
            path.append(candidates[index])
            dfs(index+1, sum+candidates[index])

            path.pop()
            while index < len(candidates)-1 and candidates[index] == candidates[index+1]:
                index+=1
            
            dfs(index+1, sum)
        dfs(0, 0)
        return res