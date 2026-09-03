class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = ""
        words = []
        word = ""

        for i in range(len(s)):
            if s[i] == " " and word == "":
                continue
            elif s[i] == " " and word != "":
                words.append(word)
                word = ""
            else:
                word += s[i]
        
        if word != "":
            words.append(word)

        res = ""
        for i in range(len(words)-1, -1, -1):
            res += words[i] + " "

        return res[0:-1]
