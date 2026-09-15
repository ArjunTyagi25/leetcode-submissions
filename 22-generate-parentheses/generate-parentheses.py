class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.res = []

        def rec(curr_string, open_bracket):
            if len(curr_string) == 2*n:
                if open_bracket == 0:
                    self.res.append(curr_string)
                return

            rec(curr_string + "(", open_bracket + 1)
            if open_bracket != 0:
                rec(curr_string + ")", open_bracket - 1)

            return

        rec("", 0)
        return self.res

        