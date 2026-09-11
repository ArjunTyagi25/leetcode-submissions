class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def rec(index_1, index_2):
            if index_1 == len(text1) or index_2 == len(text2):
                return 0

            if (index_1, index_2) in memo:
                return memo[(index_1, index_2)]

            if text1[index_1] == text2[index_2]:
                res = 1 + rec(index_1 + 1, index_2 + 1)
                memo[(index_1, index_2)] = res
                return res
            else:
                res = max(rec(index_1 + 1, index_2), rec(index_1, index_2 + 1), rec(index_1 + 1, index_2 + 1))
                memo[(index_1, index_2)] = res
                return res

        return rec(0, 0)
