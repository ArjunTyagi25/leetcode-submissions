class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [0] * 26
        self.terminal = False

class MagicDictionary:
    def __init__(self):
        self.root = TrieNode(-1)

    def buildDict(self, dictionary: List[str]) -> None:
        
        for word in dictionary:
            curr_node = self.root

            for c in word:
                if curr_node.children[ord(c) - 97] == 0:
                    curr_node.children[ord(c) - 97] = TrieNode(c)
                curr_node = curr_node.children[ord(c) - 97]
            
            curr_node.terminal = True
        

    def search(self, searchWord: str) -> bool:
        isFlipped = True

        def dfs(index, node, has_flipped):
            if index == len(searchWord):
                return node.terminal and has_flipped

            # Two choice: Either use the current character at the node or ignore the current current and recursively go down all children
            res = False
            if node.children[ord(searchWord[index]) - 97] != 0:
                res = res | dfs(index+1, node.children[ord(searchWord[index]) - 97], has_flipped)

            if not has_flipped:
                has_flipped = True
                for i in range(26):
                    if i != ord(searchWord[index]) - 97 and node.children[i] != 0:
                        res = res | dfs(index+1, node.children[i], has_flipped)
            
            return res
            


        curr_node = self.root
        return dfs(0, self.root, False)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)