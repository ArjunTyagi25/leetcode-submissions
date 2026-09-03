class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            return grid[r][c] + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0 and (r,c) not in visited:
                    res = max(res, dfs(r,c))

        return res

        