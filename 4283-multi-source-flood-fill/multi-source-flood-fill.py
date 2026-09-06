class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        q = deque()
        visited = set()
        old_grid = []
        new_grid = []
        
        for r in range(n):
            old_row = []
            new_row = []
            for c in range(m):
                old_row.append(0)
                new_row.append(0)
            old_grid.append(old_row)
            new_grid.append(new_row)
        
        for r, c, color in sources:
            old_grid[r][c] = color
            new_grid[r][c] = color
            q.append((r, c, color))
            visited.add((r,c))

        def updateGrid(r, c, adjacent_color):
            if r < 0 or c < 0 or r > n-1 or c > m-1 or (r,c) in visited or old_grid[r][c] != 0:
                return

            new_grid[r][c] = max(new_grid[r][c], adjacent_color)
            temp_visited.add((r,c))


        while q:
            temp_visited = set()
            for _ in range(len(q)):
                r, c, color = q.popleft()

                updateGrid(r+1, c, color)
                updateGrid(r-1, c, color)
                updateGrid(r, c+1, color)
                updateGrid(r, c-1, color)

            for r, c in temp_visited:
                q.append((r, c, new_grid[r][c]))
                visited.add((r,c))
        
        return new_grid

        