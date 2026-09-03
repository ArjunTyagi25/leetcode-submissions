class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        freshOranges = 0
        q = deque()
        visited = set()

        def checkForFreshFruit(r, c):
            nonlocal freshOranges

            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or grid[r][c] != 1 or (r,c) in visited:
                return

            q.append([r,c])
            visited.add((r,c))
            freshOranges -= 1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    freshOranges += 1

        if freshOranges == 0:
            return 0
            
        time = -1
        while q:
            for i in range(len(q)):
                [r,c] = q.popleft()

                grid[r][c] = 2

                checkForFreshFruit(r+1, c)
                checkForFreshFruit(r-1, c)
                checkForFreshFruit(r, c-1)
                checkForFreshFruit(r, c+1)
            time += 1

        return -1 if freshOranges != 0 else time


        