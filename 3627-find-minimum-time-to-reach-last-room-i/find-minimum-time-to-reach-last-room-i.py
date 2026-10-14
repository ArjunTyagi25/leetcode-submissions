class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROWS, COLS = len(moveTime), len(moveTime[0])
        minHeap = [(0, (0,0))] # (current time, (r,c))
        heapq.heapify(minHeap)
        visited = set()

        while minHeap:
            currTime, (r,c) = heapq.heappop(minHeap)

            if r == ROWS-1 and c == COLS-1:
                return currTime

            for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr > ROWS-1 or nc > COLS-1 or (nr,nc) in visited:
                    continue

                visited.add((nr,nc))
                if moveTime[nr][nc] > currTime:
                    heapq.heappush(minHeap, (moveTime[nr][nc] + 1, (nr,nc)))
                else:
                    heapq.heappush(minHeap, (currTime + 1, (nr,nc)))

                