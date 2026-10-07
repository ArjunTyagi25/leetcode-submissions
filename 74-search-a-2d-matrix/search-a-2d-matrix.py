class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        L, R = 0, ROWS
        while L<R:
            M = (L+R)//2

            if matrix[M][0] > target:
                R = M
            else:
                L = M + 1

        if L == 0:
            return False
        r = L - 1

        L, R = 0, COLS
        while L<R:
            M = (L+R)//2

            if matrix[r][M] == target:
                return True
            elif matrix[r][M] > target:
                R = M
            else:
                L = M + 1

        return False
        
