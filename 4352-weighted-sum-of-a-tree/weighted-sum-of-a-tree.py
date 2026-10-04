class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)
        children = { i : [] for i in range(n)}

        for i in range(1, n):
            children[parent[i]].append(i)

        q = deque()
        q.append(0)
        nodes = []
        height = 0
        depth = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                nodes.append((node, depth))
                for child in children[node]:
                    q.append(child)

            depth += 1
            height += 1

        print(height)
        res = 0
        for node, depth in nodes:
            res += nums[node] * (height - depth + 1)

        return res


