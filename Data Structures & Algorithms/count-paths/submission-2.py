class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bottom_row = [1]*n
        for _ in range(m-1):
            current_row = [1]*n
            for i in range((n)-2, -1, -1):
                current_row[i] = bottom_row[i]+current_row[i+1]

            bottom_row = current_row
        return bottom_row[0]




























