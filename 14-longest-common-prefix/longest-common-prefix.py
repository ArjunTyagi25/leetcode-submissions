class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""

        res = ""
        j = 0
        while True:
            if j == len(strs[0]):
                return res
            curr_char = strs[0][j]
            for s in strs:
                if j == len(s) or curr_char != s[j]:
                    return res
            
            res = strs[0][:j+1]
            j += 1

        