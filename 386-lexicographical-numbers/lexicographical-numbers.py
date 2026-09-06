class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [0] * 10
        self.terminal = False

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.buildTrie(n)

        # Now that we have all numbers in the Trie, we append them to the res reading them one by one
        res = []

        def dfs(node, curr_number):
            if node != self.root:
                curr_number += node.val

            if node.terminal and curr_number:
                res.append(int(curr_number))

            for i in range(10):
                if node.children[i] != 0:
                    dfs(node.children[i], curr_number)

        dfs(self.root, "")
        return res


    def buildTrie(self, size):
        self.root = TrieNode(-1)

        nums = [str(i) for i in range(1, size+1)]

        # Iterate over each num and insert it into the Trie
        for num in nums:
            curr_node = self.root

            for n in num:
                if curr_node.children[int(n)] == 0: # The children member does not contain the child so we have to insert it
                    curr_node.children[int(n)] = TrieNode(n)
                
                curr_node = curr_node.children[int(n)]

            curr_node.terminal = True
        