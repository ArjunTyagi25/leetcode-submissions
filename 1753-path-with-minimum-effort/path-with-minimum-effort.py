class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [(0, (0,0))]  # (current effort, location)
        heapq.heapify(minHeap)
        minEffort = [[float('inf') for c in range(COLS)] for r in range(ROWS)]

        while minHeap:
            currEffort, (r, c) = heapq.heappop(minHeap)
            minEffort[r][c] = currEffort

            if r == ROWS - 1 and c == COLS - 1:
                return currEffort

            for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr > ROWS-1 or nc > COLS-1:
                    continue

                effort = abs(heights[r][c] - heights[nr][nc])

                # Struggling with this piece of code
                if max(currEffort, effort) < minEffort[nr][nc]:
                    heapq.heappush(minHeap, (max(currEffort, effort), (nr, nc)))
                    minEffort[nr][nc] = max(currEffort, effort)
