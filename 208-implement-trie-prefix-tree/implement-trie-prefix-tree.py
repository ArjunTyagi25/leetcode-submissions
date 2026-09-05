class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}  # Maps values of different children to their TrieNode
        self.terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode(-1)

    def insert(self, word: str) -> None:
        curr_node = self.root

        for s in word:
            if s not in curr_node.children:
                curr_node.children[s] = TrieNode(s)
            curr_node = curr_node.children[s]
        curr_node.terminal = True


    def search(self, word: str) -> bool:
        curr_node = self.root

        for s in word:
            if s not in curr_node.children:
                return False
            curr_node = curr_node.children[s]

        return curr_node.terminal
        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for s in prefix:
            if s not in curr_node.children:
                return False
            curr_node = curr_node.children[s]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)