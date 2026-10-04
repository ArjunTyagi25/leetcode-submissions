class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        children = { i : [] for i in range(n)}

        for parent, child in edges:
            children[parent].append(child)

        def postorder(node):
            if children[node] == []:
                return baseTime[node]

            latest, earliest = float('-inf'), float('inf')
            for child in children[node]:
                childDuration = postorder(child)
                latest = max(latest, childDuration)
                earliest = min(earliest, childDuration)

            ownDuration = latest - earliest + baseTime[node]
            return latest + ownDuration

        return postorder(0)
        