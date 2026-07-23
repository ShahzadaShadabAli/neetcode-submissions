class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        ROW, COL = len(grid), len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        distance = 0

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance
                directions = [[1, 0],[-1, 0],[0, -1],[0, 1]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r in range(ROW) and c in range(COL) and grid[r][c] != -1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
            distance+=1
