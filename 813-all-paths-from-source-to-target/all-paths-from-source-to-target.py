class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        res = []
        def dfs(node, curr_path):
            nonlocal res
            if node == n-1:
                curr_path.append(node)
                res.append(curr_path.copy())
                curr_path.pop()
                return

            curr_path.append(node)
            for nextNode in graph[node]:
                dfs(nextNode, curr_path)
            curr_path.pop()

        dfs(0, [])
        return res

