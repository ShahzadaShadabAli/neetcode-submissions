class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r not in range(ROW) or c not in range(COL) or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            return (1+dfs(r+1, c)+dfs(r-1, c)+dfs(r, c+1)+dfs(r, c-1))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(dfs(r, c), maxArea)
        return maxArea
