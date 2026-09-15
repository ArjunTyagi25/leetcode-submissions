class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = {i : [] for i in range(numCourses)}
        inDegree = [0] * numCourses

        for a, b in prerequisites:
            adj_list[a].append(b)
            inDegree[b] += 1

        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        all_prerequisites = {i : set() for i in range(numCourses)}
        while q:
            cur_course = q.popleft()

            for nxt_course in adj_list[cur_course]:
                all_prerequisites[nxt_course].add(cur_course)
                all_prerequisites[nxt_course].update(all_prerequisites[cur_course])
                inDegree[nxt_course] -= 1
                if inDegree[nxt_course] == 0:
                    q.append(nxt_course)

        res = []
        for u,v in queries:
            if u in all_prerequisites[v]:
                res.append(True)
            else:
                res.append(False)

        return res
