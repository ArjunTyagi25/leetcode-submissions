class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dist = [[0 for c in range(COLS)] for r in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r,c))
                    visited.add((r,c))

        currDist = 0
        if not q or len(visited) == ROWS * COLS:
            return -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                dist[r][c] = currDist
                grid[r][c] = 1

                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr > ROWS-1 or nc > COLS-1 or (nr,nc) in visited or grid[nr][nc] == 1:
                        continue

                    q.append((nr, nc))
                    visited.add((nr,nc))
            
            currDist += 1

        return currDist-1
        

                    