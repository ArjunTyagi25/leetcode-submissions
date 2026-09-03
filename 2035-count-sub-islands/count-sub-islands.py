class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS = len(grid2)
        COLS = len(grid2[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or ((r,c)) in visited or grid2[r][c] == 0:
                return True

            visited.add((r,c))
            res = True
            if grid1[r][c] == 0:
                res = False

            res = dfs(r+1, c) and res
            res = dfs(r-1, c) and res
            res = dfs(r, c+1) and res
            res = dfs(r, c-1) and res
            return res


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and (r,c) not in visited:
                    if dfs(r, c):
                        res += 1
        
        return res
        