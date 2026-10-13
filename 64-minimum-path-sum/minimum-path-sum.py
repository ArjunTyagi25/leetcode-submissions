class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float('inf') for c in range(COLS)] for r in range(ROWS)]
        dp[ROWS-1][COLS-1] = grid[ROWS-1][COLS-1]

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                right = float('inf')
                if c+1 <= COLS-1:
                    right = dp[r][c+1]

                bottom = float('inf')
                if r+1 <= ROWS-1:
                    bottom = dp[r+1][c]

                res = min(bottom, right)
                if res == float('inf'):
                    res = 0

                dp[r][c] = grid[r][c] + res

        return dp[0][0]