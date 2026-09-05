class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        wordDict = set(wordDict)

        def rec(start_index):
            if start_index == len(s):
                return [""]

            if start_index in memo:
                return memo[start_index]

            valid_sentences = []
            for end_index in range(start_index+1, len(s) + 1):
                word = s[start_index : end_index]

                if word in wordDict:
                    sub_sentences = rec(end_index)

                    for sub in sub_sentences:
                        if sub:
                            valid_sentences.append(word + " " + sub)
                        else:
                            valid_sentences.append(word)

            memo[start_index] = valid_sentences
            return valid_sentences

        res = rec(0)
        return res