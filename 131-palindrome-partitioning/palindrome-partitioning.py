class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def rec(i, temp):
            nonlocal res
            if i == len(s):
                res.append(temp.copy())
                return

            for j in range(i+1, len(s)+1):
                if self.isPalindrome(s, i, j):
                    temp.append(s[i:j])
                    rec(j, temp)
                    temp.pop()

            return

        rec(0, [])
        return res

    def isPalindrome(self, s, i, j):
        L, R = i, j-1

        while L<=R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False

        return True