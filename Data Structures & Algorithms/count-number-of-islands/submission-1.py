class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1. TimeSaver
        if not grid:
            return 0
        
        # 2. Initialization
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        islands = 0

        def bfs (r, c):
            # 5. Add in queue and in visited
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                # 6. define directions and pop the latest pair
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    # 7. Inspecting the neighbouring land
                    r, c = row+dr, col+dc
                    # 8. I. Neighbouring val must be land. II. must be within bounds. III. must not have been visited
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == "1":
                        # 9. visited and add in queue so that the neighbours of the neighbour can be inspected
                        q.append((r, c))
                        visited.add((r, c))

        # 3. Run a loop through every single element

        for r in range(ROWS):
            for c in range(COLS):
                # 4. I. Value is land. II. land has not been visited yet
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c) 
                    islands+=1
        return islands


