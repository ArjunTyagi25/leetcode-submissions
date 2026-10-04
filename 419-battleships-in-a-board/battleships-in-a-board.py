class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        ROWS = len(board)
        COLS = len(board[0])
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X":
                    isLeft = (c == 0) or (c > 0 and board[r][c-1] == ".")
                    isTop = (r == 0) or (r > 0 and board[r-1][c] == ".")

                    if isLeft and isTop:
                        res += 1
        
        return res


        

        