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
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        
        inDegree = {i : 0 for i in range(n)}
        for a, b in edges:
            inDegree[b-1] += 1

        edges_with_two_indegree = []
        for a, b in edges:
            if inDegree[b-1] == 2:
                edges_with_two_indegree.append([a,b])
            
        if edges_with_two_indegree == []:
            for a, b in edges:
                if not uf.union(a-1, b-1):
                    return [a, b]
        else:
            e1, e2 = edges_with_two_indegree[1]
            for a, b in edges:
                if a != e1 or b != e2:
                    if not uf.union(a-1, b-1):
                        return edges_with_two_indegree[0]
            return [e1, e2]
