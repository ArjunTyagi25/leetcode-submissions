class UnionFind:
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

        if p1 == p2:
            return False

        if self.rank[p1] <= self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        return True
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for a, b in edges:
            p1, p2 = uf.find(a-1), uf.find(b-1)

            if p1 == p2:
                return [a, b]
            else:
                uf.union(p1, p2)

