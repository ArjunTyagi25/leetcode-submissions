class Node:
    def __init__(self, key = -1, val = -1, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = Node(-1, -1)
        self.MRU = Node(-1, -1)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU
        self.nodes = {}

    def add(self, node):
        self.MRU.prev.next = node
        node.prev = self.MRU.prev

        node.next = self.MRU
        self.MRU.prev = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.remove(node)
            self.add(node)
            
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.remove(node)
        else:
            node = Node(key, value)
            self.nodes[key] = node
        
        if len(self.nodes) > self.capacity:
            node_to_delete = self.LRU.next
            self.remove(node_to_delete)
            
            del self.nodes[node_to_delete.key]

        self.add(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)