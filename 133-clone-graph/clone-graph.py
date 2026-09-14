"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new_nodes = {}

        def rec(n):
            if not n:
                return None
            if n in old_to_new_nodes:
                return old_to_new_nodes[n]

            copy = Node(n.val)
            old_to_new_nodes[n] = copy

            for neighbor in n.neighbors:
                copy.neighbors.append(rec(neighbor))

            return copy

        return rec(node)

        