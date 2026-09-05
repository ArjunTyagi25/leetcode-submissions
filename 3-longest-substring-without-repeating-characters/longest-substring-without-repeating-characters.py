class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, res = 0, 0
        unique_chars = set()

        for R in range(len(s)):
            while s[R] in unique_chars:
                unique_chars.remove(s[L])
                L += 1
        
            unique_chars.add(s[R])    
            res = max(res, R-L+1)

        return res
        