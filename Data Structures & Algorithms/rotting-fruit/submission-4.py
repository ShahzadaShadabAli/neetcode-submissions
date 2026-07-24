class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        count = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    count += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        if not count:
            return 0
        mini = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if row in range(ROW) and col in range(COL) and grid[row][col] == 1:
                        q.append((row, col))
                        grid[row][col] = 2
                        count-=1
            mini += 1
        print(grid)
        if count:
            return -1
        return mini-1 #queue loop runs one extra time