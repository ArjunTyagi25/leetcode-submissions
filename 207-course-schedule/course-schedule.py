class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list = {i : [] for i in range(numCourses)}
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
            curr_course = q.popleft()

            for next_course in adj_list[curr_course]:
                if next_course not in visited:
                    inDegree[next_course] -= 1
                    if inDegree[next_course] == 0:
                        q.append(next_course)
                        visited.add(next_course)

        if len(visited) == numCourses:
            return True
        return False

        
        