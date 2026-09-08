class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = {}

        def rec(r, c):
            if r == ROWS-1 and c in range(COLS):
                return matrix[r][c]
            
            if r not in range(ROWS) or c not in range(COLS):
                return float('inf')

            if (r,c) in memo:
                return memo[(r,c)]

            left_path_sum = rec(r+1, c-1)
            bottom_path_sum = rec(r+1, c)
            right_path_sum = rec(r+1, c+1)

            min_val = min(left_path_sum, bottom_path_sum, right_path_sum)
            if min_val == float('inf'):
                return float('inf')

            res = matrix[r][c] + min_val 
            memo[(r,c)] = res

            return res

        res = float('inf')
        for c in range(COLS):
            res = min(res, rec(0, c))
        
        return res