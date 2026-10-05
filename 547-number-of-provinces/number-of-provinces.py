class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list = { i : [] for i in range(n)}

        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 1 and r != c:
                    adj_list[r].append(c)

        visited = set()
        def dfs(node):
            visited.add(node)

            for nextCity in adj_list[node]:
                if nextCity not in visited:
                    dfs(nextCity)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res