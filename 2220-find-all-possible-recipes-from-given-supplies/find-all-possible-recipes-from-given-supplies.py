class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        suppliesSet = set(supplies)
        recipesSet = set(recipes)

        adj_list = {}
        inDegree = {}
        for recipe in recipes:
            adj_list[recipe] = []
            inDegree[recipe] = 0
        
        for ingredient in ingredients:
            for i in ingredient:
                adj_list[i] = []
                inDegree[i] = 0
        
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                adj_list[ingredients[i][j]].append(recipes[i])
                inDegree[recipes[i]] += 1

        q = deque()
        visited = set()
        for k, v in inDegree.items():
            if v == 0:
                q.append(k)
                visited.add(k)

        res = []
        while q:
            item = q.popleft()

            if item in suppliesSet:
                for itemUsedIn in adj_list[item]:
                    if itemUsedIn not in visited:
                        inDegree[itemUsedIn] -= 1
                        if inDegree[itemUsedIn] == 0:
                            q.append(itemUsedIn)
                            visited.add(itemUsedIn)
            elif item in recipesSet:
                res.append(item)
                for itemUsedIn in adj_list[item]:
                    if itemUsedIn not in visited:
                        inDegree[itemUsedIn] -= 1
                        if inDegree[itemUsedIn] == 0:
                            q.append(itemUsedIn)
                            visited.add(itemUsedIn)

        return res