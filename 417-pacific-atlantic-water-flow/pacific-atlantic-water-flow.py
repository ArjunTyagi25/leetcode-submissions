class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        '''
        1. From the left edge and top edge, mark all cells that have a height greater than the current cell's height. These cells can flow into the Pacific.
        2. From the right edge and bottom edge, mark all cells that have a height greater than the current cell's height. These cells can flow into the Atlantic.
        3. Iterate over the grid and collect all cells that can flow into both the Pacific and the Atlantic.
        '''
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, curr_height, ocean):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in ocean or heights[r][c] < curr_height:
                return

            ocean.add((r,c))
            dfs(r+1, c, heights[r][c], ocean) 
            dfs(r-1, c, heights[r][c], ocean) 
            dfs(r, c+1, heights[r][c], ocean) 
            dfs(r, c-1, heights[r][c], ocean) 

            return

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS-1, heights[r][COLS-1], atl)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS-1, c, heights[ROWS-1][c], atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res