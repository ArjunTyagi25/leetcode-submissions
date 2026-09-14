class Solution:
    def minSteps(self, n: int) -> int:

        memo = {}
        def rec(curr_len, clip_len):
            if curr_len == n:
                return 0
            
            if curr_len > n:
                return float('inf')

            if (curr_len, clip_len) in memo:
                return memo[(curr_len, clip_len)]

            # Copy all character from screen to clipboard, if screen is different from the clipboard
            if curr_len == clip_len:
                copy = float('inf')
            else:
                copy = rec(curr_len, curr_len)

            # Paste all character from clipboard to screen, if clipboard is not empty
            if clip_len == 0:
                paste = float('inf')
            else:
                paste = rec(curr_len + clip_len, clip_len)
        
            res = 1 + min(copy, paste)
            memo[(curr_len, clip_len)] = res

            return res

        return rec(1, 0)