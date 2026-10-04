class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        adj_list = { i : [] for i in range(n)}

        for i in range(n):
            keys = rooms[i]
            for key in keys:
                adj_list[i].append(key)

        visited = set()

        def dfs(room):
            visited.add(room)
            for key in adj_list[room]:
                if key not in visited:
                    dfs(key)

            return

        dfs(0)
        return len(visited) == n
        