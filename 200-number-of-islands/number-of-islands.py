class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Approach 1: DFS
        '''
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in visited or grid[r][c] == "0":
                return

            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return

        num_of_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    num_of_islands += 1
                    dfs(r, c)

        return num_of_islands


        