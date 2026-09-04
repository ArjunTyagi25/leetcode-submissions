# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)

        def get_outgoing_edges(child, parent=None):
            if not child:
                return

            if parent:
                graph[child.val].append(parent.val)
                graph[parent.val].append(child.val)

            get_outgoing_edges(child.left, child)
            get_outgoing_edges(child.right, child)

        get_outgoing_edges(root, None)

        q = deque()
        visited = set()
        q.append(target.val)
        visited.add(target.val)

        curr_dist = 0
        res = []
        while q:
            for i in range(len(q)):
                node_val = q.popleft()

                if curr_dist == k:
                    res.append(node_val)
                else:
                    for neighbor in graph[node_val]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)

            curr_dist += 1
            if curr_dist > k:
                break

        return res
