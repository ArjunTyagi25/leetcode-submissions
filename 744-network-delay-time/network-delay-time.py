class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        Create the adjacency list
        Perform BFS from the target order
        At each level, keep track of max time
        After BFS, if visited does not contain all nodes, return -1. Else, return the res
        '''

        adj_list = {i : [] for i in range(1, n+1)}
        for source, dest, time in times:
            adj_list[source].append([dest, time])

        minHeap = [(0, k)]
        res = {}
        heapq.heapify(minHeap)
        
        while minHeap:
            for i in range(len(minHeap)):
                curr_time, src = heapq.heappop(minHeap)

                if src in res:
                    continue

                res[src] = curr_time

                for dest, time in adj_list[src]:
                    if dest not in res:
                        heapq.heappush(minHeap, (curr_time + time, dest))
            
        if len(res) != n:
            return -1
            
        minTime = 0
        for i in range(1, n+1):
            minTime = max(minTime, res[i])
        return minTime