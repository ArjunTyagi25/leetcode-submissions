class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digitsMapping = {"2" : ["a", "b", "c"],
                         "3" : ["d", "e", "f"],
                         "4" : ["g", "h", "i"],
                         "5" : ["j", "k", "l"],
                         "6" : ["m", "n", "o"],
                         "7" : ["p", "q", "r", "s"],
                         "8" : ["t", "u", "v"],
                         "9" : ["w", "x", "y", "z"]}

        res = []

        def backtrack(i, curr_comb):
            if i == len(digits):
                res.append(curr_comb)
                return

            number = digits[i]
            for c in digitsMapping[number]:
                backtrack(i+1, curr_comb + c)

        backtrack(0, "")
        return res
        