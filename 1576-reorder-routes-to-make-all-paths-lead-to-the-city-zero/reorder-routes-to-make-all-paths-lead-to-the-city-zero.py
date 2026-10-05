class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adjList = { i : [] for i in range(n)}
        forwardConnections = set()
        for a, b in connections:
            adjList[a].append(b)
            adjList[b].append(a)
            forwardConnections.add((a,b))

        def dfs(city, parent):
            res = 0
            for nextCity in adjList[city]:
                if nextCity != parent:
                    res += dfs(nextCity, city)
                    if (city, nextCity) in forwardConnections:
                        res += 1

            return res

        return dfs(0, -1)