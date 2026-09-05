class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordDict = set(wordDict)

        def rec(start_index):
            if start_index == len(s):
                return True
            if start_index in memo:
                return memo[start_index]

            for end_index in range(start_index+1, len(s)+1):
                sub_string = s[start_index : end_index]

                if sub_string in wordDict:
                    if end_index in memo:
                        if memo[end_index]:
                            return True
                    else:
                        memo[end_index] = rec(end_index)
                        if memo[end_index]:
                            return True

            memo[start_index] = False
            return False

        return rec(0)
