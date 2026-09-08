class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            # Encountered water so return 1 that be added to the perimeter
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or grid[r][c] == 0:
                return 1
            # Encountered an already visited cell so return 0
            if (r,c) in visited:
                return 0

            visited.add((r,c))
            return dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    return dfs(r, c)

        