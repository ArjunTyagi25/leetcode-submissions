class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            total = grid[r][c] + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c-1) + dfs(r, c+1)

            return total

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0 and (r,c) not in visited:
                    total = dfs(r,c)
                    if total % k == 0:
                        res += 1

        return res