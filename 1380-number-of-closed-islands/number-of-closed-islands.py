class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in visited or grid[r][c] == 1:
                return

            visited.add((r,c))
            grid[r][c] = 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return 

        for r in range(ROWS):
            if grid[r][0] == 0 and (r,0) not in visited:
                dfs(r, 0)
            if grid[r][COLS-1] == 0 and (r, COLS-1) not in visited:
                dfs(r, COLS-1)

        for c in range(COLS):
            if grid[0][c] == 0 and (0, c) not in visited:
                dfs(0, c)
            if grid[ROWS-1][c] == 0 and (ROWS-1, c) not in visited:
                dfs(ROWS-1, c)

        visited = set()
        num_island = 0
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if grid[r][c] == 0 and (r,c) not in visited:
                    num_island += 1
                    dfs(r,c)

        return num_island