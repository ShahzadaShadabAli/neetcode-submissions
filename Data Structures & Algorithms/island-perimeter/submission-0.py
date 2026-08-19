class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            nonlocal res
            if (r, c) in visited:
                return 0
            if r not in range(ROW) or c not in range(COL) or grid[r][c] == 0:
                return 1
            visited.add((r, c))
            res = dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            return res
           
            
            
                

        for r in range(ROW):
            for c in range(COL):
                if (r, c) not in visited and grid[r][c] == 1:
                    return dfs(r, c)
        return 0
                