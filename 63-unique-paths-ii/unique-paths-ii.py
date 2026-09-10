class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        memo = {}

        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
            
        def rec(r, c):
            if r == ROWS-1 and c == COLS-1:
                return 1

            if r > ROWS-1 or c > COLS-1 or obstacleGrid[r][c] == 1:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]

            res = rec(r+1, c) + rec(r, c+1)
            memo[(r,c)] = res
            return res

        return rec(0, 0)
        