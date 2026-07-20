class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # Step 1: Initialize the bottom row with all 1s.
        # # There is only 1 way to reach the end from any cell on the bottom edge.
        # row_below = [1] * n
        
        # # Step 2: Move upward row-by-row. 
        # # We need to calculate the paths for the remaining (m - 1) rows.
        # for _ in range(m - 1):
            
        #     # The rightmost column of any row is always 1 (can only go straight down).
        #     current_row = [1] * n
            
        #     # Step 3: Scan this current row from right to left.
        #     # We start at the second-to-last column (n-2) and go down to the first (0).
        #     for col in range(n - 2, -1, -1):
        #         # Number of ways = (cell to the right) + (cell directly below)
        #         current_row[col] = current_row[col + 1] + row_below[col]
            
        #     # Step 4: The row we just finished now becomes the "row below" 
        #     # for the next iteration as we keep climbing up.
        #     row_below = current_row
            
        # # Once we've climbed all the way to the top, index 0 is the start position.
        # return row_below[0]






























        bottomRow = [1]*n
        for _ in range(m-1):
            currRow = [1]*n
            for j in range((n-2), -1, -1):
                currRow[j] = bottomRow[j] + currRow[j+1]
            bottomRow = currRow
        return bottomRow[0]