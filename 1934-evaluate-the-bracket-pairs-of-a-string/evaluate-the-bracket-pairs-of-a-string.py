class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_dict = {}
        for key, val in knowledge:
            knowledge_dict[key] = val

        res = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == "(":
                key = ""
                i += 1
                while s[i] != ")":
                    key = key + s[i]
                    i += 1

                if key in knowledge_dict:
                    res.append(knowledge_dict[key])
                else:
                    res.append("?")
            else:
                res.append(c)
            i += 1

        return ''.join(res)
        