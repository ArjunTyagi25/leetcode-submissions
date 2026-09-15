class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            L, R = i, i
            while L>=0 and R<=len(s)-1 and s[L] == s[R]:
                if R-L+1 > resLen:
                    res = s[L:R+1]
                    resLen = R-L+1
                L -= 1
                R += 1
            
            L, R = i, i+1
            while L>=0 and R<=len(s)-1 and s[L] == s[R]:
                if R-L+1 > resLen:
                    res = s[L:R+1]
                    resLen = R-L+1
                L -= 1
                R += 1

        return res
        