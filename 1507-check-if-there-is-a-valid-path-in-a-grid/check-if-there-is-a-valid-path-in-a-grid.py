class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        if ROWS == 1 and COLS == 1:
            return True

        def dfs(r, c, previous_cell_exit):
            if r == ROWS-1 and c == COLS-1:
                if previous_cell_exit == "B" and grid[r][c] in [2, 5, 6]:
                    return True
                elif previous_cell_exit == "R" and grid[r][c] in [1, 3, 5]:
                    return True
                else:
                    return False

            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in visited:
                return False

            visited.add((r,c))
            res = False
            if previous_cell_exit == "B":
                if grid[r][c] == 2:
                    res = dfs(r+1, c, "B")
                elif grid[r][c] == 5:
                    res = dfs(r, c-1, "L")
                elif grid[r][c] == 6:
                    res = dfs(r, c+1, "R")
            elif previous_cell_exit == "T":
                if grid[r][c] == 2:
                    res = dfs(r-1, c, "T")
                elif grid[r][c] == 3:
                    res = dfs(r, c-1, "L")
                elif grid[r][c] == 4:
                    res = dfs(r, c+1, "R")
            elif previous_cell_exit == "L":
                if grid[r][c] == 1:
                    res = dfs(r, c-1, "L")
                elif grid[r][c] == 4:
                    res = dfs(r+1, c, "B")
                elif grid[r][c] == 6:
                    res = dfs(r-1, c, "T")
            else:
                if grid[r][c] == 1:
                    res = dfs(r, c+1, "R")
                elif grid[r][c] == 3:
                    res = dfs(r+1, c, "B")
                elif grid[r][c] == 5:
                    res = dfs(r-1, c, "T")

            visited.remove((r,c))
            return res

        if grid[0][0] == 1 or grid[0][0] == 6:
            return dfs(0, 1, "R")
        elif grid[0][0] == 2 or grid[0][0] == 3:
            return dfs(1, 0, "B")
        elif grid[0][0] == 5:
            return False
        else:
            return dfs(1, 0, "B") or dfs(0, 1, "R")

        


'''
If current grid cell is bottom-right, return True.
At any given cell in the grid, check if the entry to current grid cell is the same as previous grid cell's exit.
If not, return False
Otherwise, recursively go in the direction where the current grid cell exits.
'''