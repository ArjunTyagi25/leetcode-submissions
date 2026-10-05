class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)

        if self.parent[p1] == self.parent[p2]:
            return False

        if self.rank[p1] <= self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        return True

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        distances = []
        n = len(points)
        uf = DSU(n)

        for i in range(n):
            for j in range(n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if i != j:
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    distances.append([dist, i, j])

        heapq.heapify(distances)
        edges = 0
        res = 0

        while edges != n - 1:
            cost, i, j = heapq.heappop(distances)

            if uf.union(i, j):
                edges += 1
                res += cost

        return res
