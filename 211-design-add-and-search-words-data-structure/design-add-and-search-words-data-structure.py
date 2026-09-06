class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.terminal = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(-1)

    def addWord(self, word: str) -> None:
        curr_node = self.root

        for s in word:
            if s not in curr_node.children:
                curr_node.children[s] = TrieNode(s)
            
            curr_node = curr_node.children[s]

        curr_node.terminal = True        

    def search(self, word: str) -> bool:
        def dfs(j, node):
            if j == len(word):
                return node.terminal

            if word[j] == ".":
                for child in node.children.values():
                    if dfs(j+1, child):
                        return True
                return False
            else:
                if word[j] not in node.children:
                    return False
                else:
                    return dfs(j+1, node.children[word[j]])
                    
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)