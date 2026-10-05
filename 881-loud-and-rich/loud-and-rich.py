class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)
        adjList = { i : [] for i in range(n)}

        for rich_guy, poor_guy in richer:
            adjList[poor_guy].append(rich_guy)

        memo = {}
        def dfs(guy):
            if guy in memo:
                return memo[guy]

            res, resQuietVal = guy, quiet[guy]
            for richerGuy in adjList[guy]:
                quieterGuy, quieterGuyVal = dfs(richerGuy)
                if quieterGuyVal < resQuietVal:
                    resQuietVal = quieterGuyVal
                    res = quieterGuy

            memo[guy] = (res, resQuietVal)
            return (res, resQuietVal)

        res = []
        for i in range(n):
            res.append(dfs(i)[0])

        return res
