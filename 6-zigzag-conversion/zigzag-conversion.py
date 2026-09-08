class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag = [] # [[], [], [], []], numRows = 4
                    #  0   1   2   3
        for r in range(numRows):
            zigzag.append([])

        r, downward = 0, True

        for c in s:
            zigzag[r].append(c)

            if downward:
                r += 1
            else:
                r -= 1

            if r == numRows:
                downward = False
                r = numRows - 2
            elif r == -1:
                downward = True
                r = 1

        res = ""
        for row in zigzag:
            for c in row:
                res += c

        return res

        
        