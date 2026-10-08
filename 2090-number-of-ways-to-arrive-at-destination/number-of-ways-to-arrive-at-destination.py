class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj_list = { i : [] for i in range(n)}

        for u, v, time in roads:
            adj_list[u].append((v, time))
            adj_list[v].append((u, time))

        minHeap = [(0, 0)] # (total time, node)
        heapq.heapify(minHeap)
        visited = set()
        shortestTime = float('inf')
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0], ways[0] = 0, 1

        while minHeap:
            currTime, node = heapq.heappop(minHeap)

            if node == n - 1:
                return ways[node] % (pow(10, 9) + 7)

            visited.add(node)
            for nextNode, time in adj_list[node]:
                if nextNode not in visited:
                    if currTime + time < dist[nextNode]:
                        dist[nextNode] = currTime + time
                        ways[nextNode] = ways[node] % (pow(10, 9) + 7)
                        heapq.heappush(minHeap, (currTime + time, nextNode))
                    elif currTime + time == dist[nextNode]:
                        ways[nextNode] = (ways[nextNode] + ways[node]) % (pow(10, 9) + 7)
                    
        

