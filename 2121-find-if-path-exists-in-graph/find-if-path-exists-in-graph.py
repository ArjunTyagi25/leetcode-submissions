class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = {i : [] for i in range(n)}

        for src, des in edges:
            adj_list[src].append(des)
            adj_list[des].append(src)

        visited = set()

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)
            for child in adj_list[node]:
                if child not in visited:
                    if dfs(child):
                        return True

            return False

        return dfs(source)
        