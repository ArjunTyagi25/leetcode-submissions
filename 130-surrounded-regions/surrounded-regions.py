class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        '''
        Iterate through each node between rows [1, R-1] and cols [1, C-1]. 
        If that node is not visited, perform a dfs from that node.

        In dfs function, base cases will be:
        - If you reach an "X" or a visited node, return True (True meaning everything is fine)
        - If you reach an "O" and that too at the edge, return False (False meaning we cannot update the region since we reached an edge with "O")
        - Perform dfs on all 4 directions. If we receive True from all four directions, update the current node to "X" and return True. Otherwise, return False
        '''
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c):
            # Base case 1: If I am out of bound or my current location is X or if I have visited this location before, just return
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or board[r][c] == "X" or (r,c) in visited:
                return

            # Since my current location is not "X", mark it as "T" and add to visited
            board[r][c] = "T"
            visited.add((r,c))

            # Continue DFS in all four directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"