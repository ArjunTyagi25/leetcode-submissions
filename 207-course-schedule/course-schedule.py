class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = { i : [] for i in range(numCourses)}
        inDegree = [0] * numCourses
        for a, b in prerequisites:
            adj_list[b].append(a)
            inDegree[a] += 1

        q = deque()
        visited = set()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
                visited.add(i)

        while q:
            course = q.popleft()
            
            for nextCourse in adj_list[course]:
                if nextCourse not in visited:
                    inDegree[nextCourse] -= 1
                    if inDegree[nextCourse] == 0:
                        q.append(nextCourse)
                        visited.add(nextCourse)

        if len(visited) == numCourses:
            return True
        return False
