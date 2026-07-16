class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # 1.set used for quick search
        path = set()

        def dfs(r, c, i):
            # 3. Word found case
            if i == len(word):
                return True

            # 4. i-if the row and col are out of bound 
            #ii- if the current letter does not matches the letter in sequnce of the word to be searched 
            #iii-if the current path is already explored

            if r < 0 or c < 0 or r == ROWS or c == COLS or word[i] != board[r][c] or (r, c) in path:
                return False

            # 5. add the current cell in the path, branch of into all adjacent cells and remove the cells
            path.add((r, c))
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            path.remove((r, c))
            return res

        #2. The start point of the word can be any cell so check every single cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False











































