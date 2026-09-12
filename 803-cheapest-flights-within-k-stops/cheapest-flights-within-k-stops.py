class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {i : [] for i in range(n)}

        for s, d, c in flights:
            adj_list[s].append((c, d))

        minHeap = [(0, src, 0)]   # (cost, src, stops)
        heapq.heapify(minHeap)
        best_stops = {}

        while minHeap:
            curr_cost, node, stops = heapq.heappop(minHeap)

            if node == dst:
                return curr_cost

            if stops > k:
                continue

            if node in best_stops and best_stops[node] < stops:
                continue
            best_stops[node] = stops
            for c, d in adj_list[node]:
                heapq.heappush(minHeap, (curr_cost + c, d, stops + 1))

        return -1