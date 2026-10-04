class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        adj_list = { i : [] for i in range(n)}

        for i in range(n):
            childNodes = graph[i]
            for childNode in childNodes:
                adj_list[i].append(childNode)

        safeNodes = set()
        unsafeNodes = set()
        terminalNodes = set()

        for i in range(n):
            if adj_list[i] == []:
                terminalNodes.add(i)

        def dfs(node, curr_path):
            if node in terminalNodes or node in safeNodes:
                return True

            if node in unsafeNodes or node in curr_path:
                return False

            curr_path.add(node)
            isSafe = True
            for childNode in adj_list[node]:
                if childNode not in curr_path:
                    if not dfs(childNode, curr_path):
                        unsafeNodes.add(node)
                        curr_path.remove(node)
                        return False
                else:
                    return False

            curr_path.remove(node)
            safeNodes.add(node)
            return True

        res = []
        for i in range(n):
            if dfs(i, set()):
                res.append(i)

        return res
            