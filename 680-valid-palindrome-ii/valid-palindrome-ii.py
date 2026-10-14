class Solution:
    def validPalindrome(self, s: str) -> bool:
        isDeleted = False
        def checkPalindrome(L, R):
            nonlocal isDeleted
            if L >= R:
                return True

            if s[L] == s[R]:
                return checkPalindrome(L+1, R-1)
            else:
                if isDeleted:
                    return False
                else:
                    isDeleted = True
                    return checkPalindrome(L+1, R) or checkPalindrome(L, R-1)

        return checkPalindrome(0, len(s)-1)  