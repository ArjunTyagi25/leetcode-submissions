class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for i in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for s, d, w in edges:
            dist[s][d] = w
            dist[d][s] = w

        # For each possible intermediate node
        for k in range(n):
            # For each possible starting node:
            for i in range(n):
                # For each possible destination node:
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        min_city_count = float('inf')
        res = 0
        for i in range(n):
            curr_city_count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    curr_city_count += 1
            
            if curr_city_count <= min_city_count:
                res = i
                min_city_count = curr_city_count

        return res
        