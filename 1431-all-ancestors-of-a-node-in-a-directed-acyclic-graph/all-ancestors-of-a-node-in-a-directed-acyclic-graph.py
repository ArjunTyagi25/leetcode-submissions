class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        children = { i : [] for i in range(n)}
        parent = { i : [] for i in range(n)}

        for p, c in edges:
            children[p].append(c)
            parent[c].append(p)

        q = deque()
        inDegree = [0 for i in range(n)]
        for node in parent:
            inDegree[node] = len(parent[node])
            if inDegree[node] == 0:
                q.append(node)

        res = [set() for i in range(n)]
        while q:

            for _ in range(len(q)):
                node = q.popleft()

                for child in children[node]:
                    res[child] = res[child] | res[node] | {node}
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        q.append(child)


        for i in range(len(res)):
            res[i] = sorted(list(res[i]))
        return res